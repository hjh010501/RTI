from . import db as DB
from RTI.feature.disk import *
import datetime

class per_disk(DB.Document):
    p = DB.FloatField(required=True)
    used = DB.FloatField(required=True)
    unused = DB.FloatField(required=True)
    s = DB.FloatField(required=True)
    t = DB.DateTimeField(required=True)

def per_disk_upload(diskpercent, diskused, diskunused, disksize):
    per_disk(p=diskpercent, used=diskused, unused=diskunused, s=disksize, t=datetime.datetime.now()).save()

def get_disk_info():
    list = per_disk.query.descending('t').limit(19).all()[::-1]
    values = []
    for value in list:
        values.append(round(value.p))
    return values