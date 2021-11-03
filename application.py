"""
This script runs the FlaskTemplate application using a development server.
"""
import os
import time
preInit = 'bash ./FlaskTemplate/./preinit.sh'
os.system(preInit)
time.sleep(240)

os.system('python flapp.py')



