# Database for Watermelon Tasting 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    """A User and their Watermelon Reservations."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Coulmn(db.String, nullable=False, unique=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User's First Name={self.fname}, User's Username={self.user_name}>"

if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
    db.create_all()