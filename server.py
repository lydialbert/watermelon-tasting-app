#Server for Watermelon Tasting App.

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined

import os
import requests
import crud
import calendar

app = Flask(__name__)
app.secret_key = "SECRET"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def welcome():
    """View the Welcome Page."""

    return render_template("login.html")

@app.route('/create-user', methods=['POST'])
def new_user():
    """Create a New User in the Database."""

    first_name = request.form.get("fname")
    username = request.form.get("username")

    user = crud.create_user(first_name, username)

    return redirect('/')

@app.route('/login', methods=['POST'])
def logging_in():
    """Process a User Login."""

    return render_template("bookings.html")

@app.route('/search', methods=['POST'])
def present_bookings():
    """View Watermelon Tastings for Booking."""

    start_time = request.form.get("start-time")
    end_time = request.form.get("end-time")
    date = request.form.get("date")

    avaiable_reservations = ['time']

    if start_time and end_time not in avaiable_reservations:
        flash("Sorry their are no reservations available for that time.")
    else:
        return render_template("tastings.html")

@app.route('/book', methods=['POST'])
def add_bookings():
    """Add a Reservation to Database."""

    #add a reservation using a crud function
    #add a crud function to look at ALL of a users reservations
    #if reservation.time == time1 and reservation.time == time2:
        #flash("Can only book one reservation per time.")
    #else:
        #return render_template("tastings.html")

@app.route('/reservations', methods=['POST'])
def view_bookings():
    """View all Reservations."""

    return render_template("reservations.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)