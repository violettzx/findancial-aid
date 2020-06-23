from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, login_required, current_user, logout_user
from app import app, db, bcrypt
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/start')
def start():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('start.html', title="Get Started")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Incorrect email or password.', 'danger')
    return render_template('login.html', title='Log In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created. You are now able to login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/home')
@login_required
def home():
    return render_template('home.html', title='Home')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('start'))
