# backend/app/__init__.py
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

from . import models
from . import views
