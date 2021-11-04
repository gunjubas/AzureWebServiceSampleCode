"""
Routes and views for the flask application.
"""
from flask import render_template
from FlaskTemplate import app
import os
import subprocess
from datetime import datetime
from base64 import urlsafe_b64encode


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    # cmd = "python query.py"
    cmd = 'python FlaskTemplate/query.py'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    queryOut = str(stdout)
    return render_template(
        'about.html',
        title='About',
        year = datetime.now().year,
        message = 'Test message',
        # message = str(retrieved_secret.value),
        message2 = queryOut,
        # message2 = '123',
        message3 = os.environ['WEBSITE_SITE_NAME']
    )
