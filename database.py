from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)#for some reason int dosent exist or dosent work also string can capture any hyphens or extensions such as +1
    email = db.Column(db.String(100), nullable=False) # wrote this down before i forget it|||||| the hashtag is the character for comments
    details = db.Column(db.Text, nullable=True)

def initialize_database(app):
    """Connect the database to Flask and create missing tables."""

    db.init_app(app)

    with app.app_context():
        db.create_all()