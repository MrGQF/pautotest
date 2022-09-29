import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dbPath = os.path.abspath('./src/Storage/sh_daily.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbPath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
