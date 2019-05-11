from . import db as DB
from RTI.feature.cpu import *
from mongoalchemy.session import Session

import datetime

class per_cpu(DB.Document):
    _id = DB.ObjectIdField
    n = DB.FloatField(required=True)
    t = DB.DateTimeField(required=True)

def per_cpu_upload(p):
    per_cpu(n=p, t=datetime.datetime.now()).save()

def get_cpu_info():
    list = per_cpu.query.descending('t').limit(19).all()[::-1]
    values = []
    for value in list:
        values.append(round(value.n))
    return values