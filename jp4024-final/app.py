# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill

Name: Janelle Ponnor
UNI: jp4024
This file contains different routes to the home page, assignments page,
and classes page.
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

#Route to assignments page
@app.route("/1006assignments")
def test123():
    return render_template("1006assignments.html")

#Route to classes page
@app.route("/1006classes")
def columbia():
    return render_template("1006classes.html")

#start the server
if __name__ == "__main__":
    app.run()