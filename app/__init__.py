from flask import Flask

app = Flask(__name__)

# Load configuration from environment variable or a configuration file
app.config.from_object('config.Config')

# Initialize Flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import views (routes) after initializing app
from app import routes
