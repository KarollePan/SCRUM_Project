from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.rooms.forms import AddRoomForm, EditRoomForm
from app.models import Room
from app.funcs import save_picture
from app import db
from flask_login import current_user, login_user, logout_user, login_required

rooms = Blueprint('rooms', __name__)

@rooms.route('/all_rooms')
def all_rooms():
    return 'All rooms page'

@rooms.route('/new_room', methods=['GET', 'POST'])
@login_required
def new_room():
    form = AddRoomForm()
    if form.validate_on_submit():
        image_file = 'default.jpg'
        if form.image.data:
            image_file = save_picture(form.image.data)
  
        room = Room(
            title=form.title.data,
            description=form.description.data,
            image=image_file,
            price=form.price.data,
        )
        db.session.add(room)
        db.session.flush()
        new_id = room.id
        db.session.commit()
        flash('Room was added successfully', 'success')
        return redirect(url_for('rooms.room', id=new_id))
    return render_template('rooms/new_room.html', title='Add room', form=form)

@rooms.route('/room/<id>', methods=['GET', 'POST'])
def room(id):
    room = Room.query.get(id)
    return render_template('rooms/room.html', title=room.title.title(), room=room)

@rooms.route('/room/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_room(id):
    room = Room.query.get(id)
    form = EditRoomForm(obj=room)
    if request.method == 'GET':
        form.populate_obj(room)
    elif request.method == 'POST':
        if form.update.data and form.validate_on_submit():
            room.title = form.title.data
            room.description = form.description.data
            if form.image.data:
                room.image = save_picture(form.image.data)
            room.price = form.price.data
            db.session.commit()
            flash ('Update was successful', 'success')
            return redirect(url_for('rooms.room', id=id))
        if form.cancel.data:
            return redirect(url_for('rooms.room', id=id))
    return render_template('rooms/edit_room.html', title='Edit room', form=form)

@rooms.route('/room/<id>/delete', methods=['GET', 'POST'])
@login_required
def delete_room(id):
    if Room.query.filter_by(id=id).delete():
        db.session.commit()
        flash ('Room has been deleted', 'success')
        return redirect(url_for('main.index'))
    return redirect(url_for('rooms.room', id=id))  

@rooms.route('/search', methods=['GET', 'POST'])
def search():
    rooms = None
    target_string = request.form['search']

    rooms = Room.query.filter(Room.title.contains(target_string)).all()

    if target_string == '':
        search_msg = f'No matching records found - displaying all {len(rooms)} rooms'
        color = 'danger'
    else:
        search_msg = f'{len(rooms)} rooms found'
        color = 'success'
    return render_template('rooms/search.html', 
        title='Search result', rooms=rooms, 
        search_msg=search_msg, color=color
    )
