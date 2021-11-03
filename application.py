"""
This script runs the FlaskTemplate application using a development server.
"""
import os
import time
from os import environ
from FlaskTemplate import app

preInit = 'bash ./FlaskTemplate/./preinit.sh'
os.system(preInit)
time.sleep(240)
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT)
