#Server for Watermelon Tasting App.

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db

import os
import requests

@app.route('/')
def welcome():
    """View the Welcome Page."""

    render_template("login.html")

@app.route('/create-user', methods=['POST'])
def new_user():
    """Create a New User in the Database."""

    first_name = request.form.get("fname")
    username = request.form.get("username")


@app.route('/login')
def login():
    """Process a User Login."""
