from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from db import db
from forms import ProjectForm, LoginForm
from models import Project, User
import os

def index():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)

@login_required
def admin():
    projects = Project.query.all()
    return render_template('admin.html', projects=projects)

@login_required
def admin_dashboard():
    projects = Project.query.all()
    return render_template('admin_dashboard.html', projects=projects)

@login_required
def add_project():
    from app import app
    form = ProjectForm()
    if form.validate_on_submit():
        image_filename = 'default.png' 
        if form.image.data:
            image_filename = form.image.data.filename
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            mini_description=form.mini_description.data,
            stack_used=form.stack_used.data,
            link=form.link.data,
            link_github=form.link_github.data,
            image=image_filename
        )
        db.session.add(new_project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('admin'))
    return render_template('add_project.html', form=form)

@login_required
def edit_project(project_id):
    from app import app
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    
    if form.validate_on_submit():
        if form.image.data:
            if project.image and project.image != 'default.png':
                old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], project.image)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            image_filename = form.image.data.filename
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            project.image = image_filename
        elif 'delete_image' in request.form:
            if project.image and project.image != 'default.png':
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], project.image)
                if os.path.exists(image_path):
                    os.remove(image_path)
                project.image = 'default.png'
        
        project.name = form.name.data
        project.description = form.description.data
        project.mini_description = form.mini_description.data
        project.stack_used = form.stack_used.data
        project.link = form.link.data
        project.link_github = form.link_github.data
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin'))
    
    return render_template('edit_project.html', form=form, project=project)

@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin'))

def login():
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
def delete_project_image(project_id):
    from app import app
    project = Project.query.get_or_404(project_id)
    if project.image and project.image != 'default.png':
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], project.image)
        if os.path.exists(image_path):
            os.remove(image_path)
        project.image = 'default.png'
        db.session.commit()
        flash('Image deleted successfully!', 'success')
    else:
        flash('Cannot delete default image.', 'warning')
    return redirect(url_for('edit_project', project_id=project.id))

@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
