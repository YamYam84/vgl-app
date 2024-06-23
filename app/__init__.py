from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from flask_talisman import Talisman

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SESSION_COOKIE_SECURE'] = True  # Only send cookie over HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to the cookie
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Prevent CSRF

# Content Security Policy configuration
csp = {
    'default-src': [
        '\'self\'',  # Allow content only from the same origin
    ],
    'script-src': [
        '\'self\'',  # Allow scripts only from the same origin
        #'cdnjs.cloudflare.com'  # example - allows scripts from CDNJS
    ],
    'style-src': [
        '\'self\'',  # Allow styles only from the same origin
    ],
    'img-src': [
        '\'self\'',  # Allow images only from the same origin
    ],
    'font-src': [
        '\'self\'',  # Allow fonts only from the same origin
    ],
    'connect-src': [
        '\'self\'',  # Allow AJAX requests only to the same origin
    ],
    'frame-src': [
        '\'self\'',  # Allow frames only from the same origin
    ]
}

talisman = Talisman(app, content_security_policy=csp)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes

def create_app():
    with app.app_context():
        from init_db import initialize_db
        initialize_db()

    return app

if not os.path.exists('site.db'):
    create_app()
