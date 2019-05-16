#!/usr/bin/env python3
from flask import Flask, request

# create a virtual environment  python3 -m venv virtual-environment-name followed by python3 -m venv venv

# name of main module/package of application
app = Flask(__name__) # used tot determine the location of application


# Routes and View Functions (Mapping of URLs to Python function)
@app.route('/') # register function as handler to be invoked when certain event occur. This is a handler for the root URL alternative way is to use  app.add_url_rule() method
def index(): # view function
    return '<h1> Hello Flask </h1>' # return value of the view function

@app.route('/user/<name>') # Flask supports variable sections to define a route that has a dynamic component (string, int, float, and path supported)
def user(name):
    return ('<h1> Hello, {}!'.format(name)) 

@app.route('/us')
def us():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

# NEVER enable debug on a production server
#app.run(debug=True)