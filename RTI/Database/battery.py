from . import db as DB
from RTI.Feature.battery import *


class per_battery(DB.Document):
    p = DB.FloatField()
    status = DB.StringField()


def per_battery_upload(batterypercent, batterystatus):
    per_battery(p=batterypercent, status=batterystatus).save()
