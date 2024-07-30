from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from db import db
from forms import ProjectForm, LoginForm

def index():
    from models import Project
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@login_required
def admin():
    from models import Project
    form = ProjectForm()
    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            link=form.link.data,
            image=form.image.data
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('admin.html', form=form)

def login():
    from models import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
