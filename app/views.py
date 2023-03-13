"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash, session, abort,send_from_directory
from app.forms import AddPropertyForm
from werkzeug.utils import secure_filename
from app.models import AddProperty







###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kyle Henry")

@app.route('/property', methods=["GET", "POST"] )
def NewProperty():
    form= AddPropertyForm()

    if request.method == 'POST' and form.validate():
        title= form.title.data
        description=form.description.data
        No_Rooms= form.No_Rooms.data
        No_bathrooms=form.No_bathrooms.data
        price=form.price.data
        property_type=form.property_type.data
        location=form.location.data
        
        file = form.photo.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
      

        property=AddProperty(title=title,description=description,No_Rooms=No_Rooms,No_bathrooms=No_bathrooms,price=price,property_type=property_type,location=location,photo=filename)

        db.session.add(property)
        db.session.commit()

        flash('Property added', 'success')
        return redirect(url_for('display_properties'))
    return render_template('form.html',form=form)



def  get_uploaded_images():
    path = os.path.join(os.getcwd(),app.config["UPLOAD_FOLDER"] )
    return [file for subdir, dirs, files in os.walk(path) for file in files]

@app.route('/uploads/<filename>')
def get_image(filename):
     
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.route('/properties')
def display_properties():
    properties = db.session.query(AddProperty).all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def display_property(propertyid):
    property = AddProperty.query.get(propertyid)
    return render_template('property.html', property=property)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
