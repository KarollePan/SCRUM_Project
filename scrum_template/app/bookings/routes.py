from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import WedBooking, TourBooking, Time
from app.bookings.forms import AddWeddingBookingForm, AddTourBookingForm, EditWeddingBookingForm, EditTourBookingForm
from app import db
from flask_login import current_user, login_user, logout_user, login_required

bookings = Blueprint('bookings', __name__)

@bookings.route('/wedbooking', methods=['GET', 'POST'])
@login_required
def wedbooking():
    # link the form
    form = AddWeddingBookingForm()
    # if form is submitted, gather the parameters from the form and store it into wedbookings
    if form.validate_on_submit():
        wedbooking = WedBooking(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            telno = form.telno.data,
            date = form.date.data,
            incl_catering = form.incl_catering.data,
            incl_flowers = form.incl_flowers.data,
            incl_carhire = form.incl_carhire.data,
            incl_visual_and_audio = form.incl_visual_and_audio.data,
            incl_photography = form.incl_photography.data
        )
        # push the new wedbooking to the database
        db.session.add(wedbooking)
        db.session.flush()
        db.session.commit()
        # display a message
        flash('Thank you, we will be in touch with you soon!', 'success')
        return redirect(url_for('bookings.wedbooking'))
    return render_template('bookings/new_wedding.html', title = 'Wedding Booking', form=form)

@bookings.route('/wedbookings', methods=['GET', 'POST'])
@login_required
def wedbookings():
    wedbookings = None
    # run a query for all wedbookings
    wedbookings = WedBooking.query.all()
    # record counter
    msg = f'{len(wedbookings)} Wedding Booking(s)'
    color = 'success'
    return render_template('bookings/wedbookings.html', title='All Wedding Bookings', wedbookings=wedbookings, msg=msg, color=color)

@bookings.route('/wedbooking/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_wedbooking(id):
    wedbooking = WedBooking.query.get(id)
    form = EditWeddingBookingForm(obj=wedbooking)
    if request.method == 'GET':
        form.populate_obj(wedbooking)
    elif request.method == 'POST':
        if form.update.data and form.validate_on_submit():
            wedbooking.first_name = form.first_name.data
            wedbooking.last_name = form.last_name.data
            wedbooking.email = form.email.data
            wedbooking.telno = form.telno.data
            wedbooking.date = form.date.data
            wedbooking.incl_catering = form.incl_catering.data
            wedbooking.incl_visual_and_audio = form.incl_visual_and_audio.data
            wedbooking.incl_photography = form.incl_photography.data
            wedbooking.incl_flowers = form.incl_flowers.data
            wedbooking.incl_carhire = form.incl_carhire.data
            db.session.commit()
            flash ('Update was successful', 'success')
            return redirect(url_for('bookings.wedbookings'))
        if form.cancel.data:
            return redirect(url_for('bookings.wedbookings'))
        if form.delete.data:
            if wedbooking.query.filter_by(id=id).delete():
                db.session.commit()
                flash ('Wedding Booking has been deleted', 'success')
                return redirect(url_for('bookings.wedbookings'))
    return render_template('bookings/edit_wedbooking.html', title='Edit Tour Booking', form=form)

@bookings.route('/tourbooking', methods=['GET', 'POST'])
@login_required
def tourbooking():
    # link the form
    form = AddTourBookingForm()
    # populate the select field with time hours
    form.time_id.choices = [(time.id, time.hour.title()) for time in Time.query.all()]
    # if form is submitted store the parameters
    if form.validate_on_submit():
        tourbooking = TourBooking(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            telno = form.telno.data,
            date = form.date.data,
            time_id = form.time_id.data
        )
        # push the new tourbooking to the database
        db.session.add(tourbooking)
        db.session.flush()
        db.session.commit()
        # display a message
        flash('Thank you, we will be in touch with you soon!', 'success')
        return redirect(url_for('bookings.tourbooking'))
    return render_template('bookings/new_tour.html', title = 'Tour Booking', form=form)

@bookings.route('/tourbookings', methods=['GET', 'POST'])
@login_required
def tourbookings():
    tourbookings = None
    # run a query for all tour bookings
    tourbookings = TourBooking.query.all()
    # record counter
    msg = f'{len(tourbookings)} Tour Booking(s)'
    color = 'success'
    return render_template('bookings/tourbookings.html', title='All Tour Bookings', tourbookings=tourbookings, msg=msg, color=color)

@bookings.route('/tourbooking/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_tourbooking(id):
    tourbooking = TourBooking.query.get(id)
    form = EditTourBookingForm(obj=tourbooking)
    form.time_id.choices = [(time.id, time.hour.title()) for time in Time.query.all()]
    if request.method == 'GET':
        form.populate_obj(tourbooking)
    elif request.method == 'POST':
        if form.update.data and form.validate_on_submit():
            tourbooking.first_name = form.first_name.data
            tourbooking.last_name = form.last_name.data
            tourbooking.email = form.email.data
            tourbooking.telno = form.telno.data
            tourbooking.date = form.date.data
            tourbooking.time_id = form.time_id.data
            db.session.commit()
            flash ('Update was successful', 'success')
            return redirect(url_for('bookings.tourbookings'))
        if form.cancel.data:
            return redirect(url_for('bookings.tourbookings'))
        if form.delete.data:
            if tourbooking.query.filter_by(id=id).delete():
                db.session.commit()
                flash ('Tour Booking has been deleted', 'success')
                return redirect(url_for('bookings.tourbookings'))
    return render_template('bookings/edit_tourbooking.html', title='Edit Tour Booking', form=form)
