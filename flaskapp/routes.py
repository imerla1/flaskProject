from flask import render_template, url_for, flash, redirect, request
from flaskapp import db, app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and form.password.data == user.password:
            login_user(user)
            return redirect(url_for('home'))
            
        else:
            
            flash('Login Unsuccessfull please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/account', methods=["GET", "POST"])
def account():
    return "ACC PAGE"

@app.route('/logout', methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('home'))