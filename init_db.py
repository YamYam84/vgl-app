from werkzeug.security import generate_password_hash
from app.models import User, Post
from app import db

def initialize_db():
    # Create the database and the database tables
    db.create_all()

    # Optionally, add initial data to the database
    if not User.query.first():
        default_user = User(username='admin', email='admin@example.com', password=generate_password_hash('password'))
        db.session.add(default_user)
        db.session.commit()

    print("Database initialized!")
