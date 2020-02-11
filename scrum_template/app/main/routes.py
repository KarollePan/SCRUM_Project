#Coursework one
from flask import Blueprint, render_template, redirect, url_for, request
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')
    
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title = 'Contact')

@main.route('/packagedeals',methods=['GET','POST'])
def packagedeals():
    return render_template('packagedeals.html', title = 'Package Deals')
    
@main.route('/catering',methods=['GET','POST'])
def catering():
    return render_template('catering.html', title = 'Catering')
    
@main.route('/photographers',methods=['GET','POST'])
def photographers():
    return render_template('photographers.html', title = 'Photographers')

@main.route('/carhire',methods=['GET','POST'])
def carhire():
    return render_template('carhire.html', title = 'Carhire')
    
@main.route('/music',methods=['GET','POST'])
def music():
    return render_template('music.html', title = 'Music')
    
