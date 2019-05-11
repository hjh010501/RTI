from . import db as DB
from RTI.feature.memory import *
import datetime

class train_logs(DB.Document):
    logs = DB.StringField(required=True)
    epoch = DB.IntField(required=True)
    loss = DB.StringField(required=True)
    accuracy = DB.StringField(required=True)
    t = DB.DateTimeField(required=True)

def train_logs_upload(logs, epoch, loss, accuracy, t):
    train_logs(logs=logs, epoch=epoch, loss=loss, accuracy=accuracy, t=t).save()

def get_memory_info():
    list = train_logs.query.descending('t').all()[::-1]
    values = []
    for value in list:
        values.append(round(value.p))
    return values