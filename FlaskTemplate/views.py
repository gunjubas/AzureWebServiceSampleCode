"""
Routes and views for the flask application.
"""
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

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
    keyVaultName = os.environ['ConnectionString']
    KVUri = f'https://{keyVaultName}.vault.azure.net'

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    secretName = 'maksym-ganistrat-1'
    retrieved_secret = client.get_secret(secretName)
    return render_template(
        'about.html',
        title='About',
        year = datetime.now().year,
        message = str(retrieved_secret.value)
    )
