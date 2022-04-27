#Operations in Database for Watermelon App.

from model import db, User, connect_to_db

def create_user(fname, username):
    """Create and Return a User."""

    user = User(
        fname=fname,
        username=username,
    )

    return

def login_user(fname):
    """Verify a User Login."""

    return User.query.filter(User.fname == fname).first()