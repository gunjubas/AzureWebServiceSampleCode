"""
Routes and views for the flask application.
"""
import os
# import pyodbc
from datetime import datetime
from flask import render_template
from FlaskTemplate import app


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
    """Renders the about page."""
    # sqlResponse = []
    # with pyodbc.connect(os.environ['ConnectionString']) as conn:
    #     with conn.cursor() as cursor:
    #         cursor.execute("SELECT TOP (10) [Title], [FirstName], [MiddleName], [LastName], [CompanyName], [Phone], [ModifiedDate] FROM [SalesLT].[Customer]")
    #         row = cursor.fetchone()
    #         while row:
    #             sqlResponse.append('<tr>')
    #             for i in row:
    #                 sqlResponse.append(f'<td>{i}</td>')
    #             row = cursor.fetchone()
    #             sqlResponse.append('</tr>')

    return render_template(
        'about.html',
        title='About',
        year = datetime.now().year,
        message = 'Test message',
        # message = str(retrieved_secret.value),
        # message2 = str(sqlResponse[0:]),
        message2 = '123',
        message3 = os.environ['WEBSITE_SITE_NAME']
    )
