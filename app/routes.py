from flask import render_template, flash, redirect, url_for, session
from app import flask_app
from app.login_form import LoginForm
from app.login_database import LoginDatabase
from app.passenger_database import PassengerDatabase
from app.report_form import ReportForm


@flask_app.route('/index')
@flask_app.route('/')
def index():
    return render_template('index.html', title='Home')

@flask_app.route('/login/', methods=['GET', 'POST'])
def login():

    try:
        if 'username' in session:
            return redirect(url_for('index'))
    except Exception as e:
        print(e)

    form = LoginForm()
    if form.validate_on_submit():
        db = LoginDatabase()
        db.users_db_cursor.execute("SELECT * FROM users WHERE username = (?)", [form.username.data])
        try:
            user = list(db.users_db_cursor.fetchone())
        except:
            flash("Invalid username or password")
            return redirect(url_for('login'))
        if not db.compare(form.username.data, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        session['username'] = form.username.data
        session['role'] = user[3]
        flash('Logged in successfully')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@flask_app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@flask_app.route('/report', methods=['GET', 'POST'])
def report():
    form = ReportForm()
    if form.validate_on_submit():
        db = PassengerDatabase()
        db.c.execute("SELECT first_name, last_name, passport_id FROM " + form.flight_id.data)
        data = db.c.fetchall()
        return render_template('report.html', title='Report', form=form, data=data)
    return render_template('report.html', title='Report', form=form)
