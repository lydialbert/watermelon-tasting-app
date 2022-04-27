#Operations in Database for Watermelon App.

from model import db, User, connect_to_db

def create_user(fname, username):
    """Create and Return a User."""

    user = User(
        fname=fname,
        username=username,
    )

    return user