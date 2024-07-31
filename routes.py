from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import secure_filename
from db import db
from forms import ProjectForm, LoginForm
import os

def index():
    from models import Project
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@login_required
def admin():
    from app import app
    from models import Project
    form = ProjectForm()
    if form.validate_on_submit():
        filename = ''
        if form.image.data:
            file = form.image.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            link=form.link.data,
            image=filename,
            link_github=form.link_github.data
        )
        db.session.add(new_project)
        db.session.commit()
        flash('New project added successfully!', 'success')
        return redirect(url_for('admin'))
    
    projects = Project.query.all()
    return render_template('admin.html', form=form, projects=projects)

@login_required
def edit_project(project_id):
    from app import app
    from models import Project
    project = Project.query.get_or_404(project_id)
    form = ProjectForm()
    if form.validate_on_submit():
        if form.image.data:
            file = form.image.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            project.image = filename
        
        project.name = form.name.data
        project.description = form.description.data
        project.link = form.link.data
        project.link_github = form.link_github.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin'))
    elif request.method == 'GET':
        form.name.data = project.name
        form.description.data = project.description
        form.link.data = project.link
        form.link_github.data = project.link_github
    return render_template('edit_project.html', form=form, project=project)

@login_required
def delete_project(project_id):
    from models import Project
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin'))

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
