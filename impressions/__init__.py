from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('impressions.app_settings')

db = SQLAlchemy(app)

from impressions import models  # NOQA
from impressions import views  # NOQA
