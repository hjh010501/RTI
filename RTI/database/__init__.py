from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from RTI import app
import urllib.parse
from RTI.loader import database_load
import RTI.configs


DB_HOST = urllib.parse.quote_plus(RTI.configs.MONGO_HOST)
DB_PORT = urllib.parse.quote_plus(RTI.configs.MONGO_PORT)
DB_TABLE = urllib.parse.quote_plus(RTI.configs.MONGO_TABLE)
DB_NAME = urllib.parse.quote_plus(RTI.configs.MONGO_USER)
DB_PASSWORD = urllib.parse.quote_plus(RTI.configs.MONGO_PASSWORD)

app.config['MONGOALCHEMY_SERVER_AUTH'] = False
app.config['MONGOALCHEMY_SERVER'] = DB_HOST
app.config['MONGOALCHEMY_PORT'] = DB_PORT
app.config['MONGOALCHEMY_USER'] = DB_NAME
app.config['MONGOALCHEMY_PASSWORD'] = DB_PASSWORD
app.config['MONGOALCHEMY_DATABASE'] = DB_TABLE


db = MongoAlchemy(app)

database_load('battery',
              'cpu',
              'memory',
              'disk')