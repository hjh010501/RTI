from . import db as DB
from RTI.feature.memory import *
import datetime

class train_logs(DB.Document):
    epoch = DB.IntField(required=True)
    loss = DB.FloatField(required=True)
    accuracy = DB.FloatField(required=True)
    t = DB.DateTimeField(required=True)

def train_logs_upload(epoch, loss, accuracy, t):
    train_logs(epoch=epoch, loss=loss, accuracy=accuracy, t=datetime.datetime.now()).save()

def get_memory_info():
    list = train_logs.query.descending('t').all()[::-1]
    values = []
    for value in list:
        values.append(round(value.p))
    return values