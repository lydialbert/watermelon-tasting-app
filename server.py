#Server for Watermelon Tasting App.

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db

import os
import requests

app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def welcome():
    """View the Welcome Page."""

    return render_template("login.html")

@app.route('/create-user', methods=['POST'])
def new_user():
    """Create a New User in the Database."""

    first_name = request.form.get("fname")
    username = request.form.get("username")

    return re-direct('/')

@app.route('/login', methods=['POST'])
def logging_in():
    """Process a User Login."""
    
    return render_template("bookings.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)