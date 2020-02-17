from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import Enquiry, Review
from app.enquiries.forms import ContactForm
from app.reviews.forms import ReviewForm
from sqlalchemy.sql import func
from app import db
from flask_login import current_user, login_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html',  title='Home')
    
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    # link the form
    form = ContactForm()
    # if form is submitted
    if form.validate_on_submit():
        # store the parameters from the form
        enquiry = Enquiry(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            telno = form.telno.data,
            description = form.description.data
        )
        # push it to the database
        db.session.add(enquiry)
        db.session.flush()
        db.session.commit()
        # display a message
        flash('Thank you, we will be in touch with you soon!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title = 'Contact', form=form)

@main.route('/enquiries', methods=['GET', 'POST'])
@login_required
def enquiries():
    enquiries = None
    # fetch all equiries from the database
    enquiries = Enquiry.query.all()
    # record counter
    msg = f'{len(enquiries)} Enquiry(ies)'
    color = 'success'
    return render_template('enquiries.html', title='All enquiries', enquiries=enquiries, msg=msg, color=color)

@main.route('/packagedeals',methods=['GET','POST'])
def packagedeals():
    return render_template('packagedeals.html', title = 'Package Deals')

@main.route('/services', methods=['GET','POST'])
def services():
    return render_template('services.html', title = 'Services')

@main.route('/reviews', methods=['GET','POST'])
def reviews():
    reviews = None
    # running a query to get all reviews
    reviews = Review.query.all()
    # link the form
    form = ReviewForm()
    # count the average of all review ratings
    temp = db.session.query(func.avg(Review.rating).label('average'))
    # if average exists
    if temp[0].average:
        # round up the average to two decimal places
        avg = round(temp[0].average, 2) 
    else: 
        avg = 0

    if form.validate_on_submit():
        # fetch the count of current user's review (supposed to be either none or one)
        rev = Review.query.filter_by(user_id=current_user.get_id()).count()
        #if it's not 0 i.e. there's a review already written by the user
        if rev != 0:
            # display message
            flash("Can't review a book twice. Please edit/update your previous review", "warning")
        # if user hasn't written a review before, accept the parameters from the form
        else:
            review = Review(
                rating = round(form.rating.data, 2),
                text = form.text.data,
                user_id = current_user.get_id()
            )
            flash("Review has been added", "success")
            # push the review to the database
            db.session.add(review)
            db.session.commit()
        return redirect(url_for('main.reviews'))
    return render_template('reviews/reviews.html', title = 'Reviews', reviews=reviews, form=form, average=avg)

@main.route('/edit_review', methods=['GET', 'POST'])
@login_required
def edit_review():
    # fetch the current user's review
    review = Review.query.filter_by(user_id=current_user.get_id())[0]
    # link the form
    form = ReviewForm()
    # if get - display the review text in the form's text box
    if request.method == 'GET':
        form.text.data = review.text 
    # if form is submitted and post'ed - fetch the new rating/text and push it to the database
    if form.validate_on_submit() and request.method == 'POST':
        review.rating = round(form.rating.data, 2)
        review.text = form.text.data
        db.session.commit()
        return redirect(url_for('main.reviews'))
    return render_template('reviews/edit_review.html', title="Edit review", form=form)

@main.route('/delete_review/<id>', methods=['GET', 'POST'])
@login_required
def delete_review(id):
    # get the id of the review and delete it
    if Review.query.filter_by(id=id).delete():
        db.session.commit()
        flash ('Review has been deleted', 'success')
        return redirect(url_for('main.reviews'))
    return redirect(url_for('main.reviews'))  