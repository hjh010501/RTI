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

def get_train_info():
    list = train_logs.query.descending('epoch').all()[::-1]
    result = []
    for value in list:
        result.append({
            'logs': value.logs,
            'epoch': value.epoch,
            'loss': value.loss,
            'accuracy': value.accuracy,
            't': value.t
        })
    print(result)
    return result