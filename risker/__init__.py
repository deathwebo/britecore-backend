from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db_url = 'mysql://root:rootlocal@localhost/risker'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import risker.views
import risker.commands