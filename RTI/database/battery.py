from . import db as DB
from RTI.feature.battery import *
import datetime


class per_battery(DB.Document):
    p = DB.FloatField()
    status = DB.StringField()
    t = DB.DateTimeField(required=True)


def per_battery_upload(batterypercent, batterystatus):
    per_battery(p=batterypercent, status=batterystatus, t=datetime.datetime.now()).save()


def get_battery_info():
    list = per_battery.query.descending('t').limit(19).all()[::-1]
    values = []
    for value in list:
        values.append(round(value.p))
    return values