from . import db as DB
from RTI.feature.memory import *
import datetime

class per_memory(DB.Document):
    p = DB.FloatField(required=True)
    used = DB.IntField(required=True)
    unused = DB.IntField(required=True)
    t = DB.DateTimeField(required=True)

def per_memory_upload(memoryused, memoryunused, memorypercent):
    per_memory(p=memorypercent, used=memoryused, unused=memoryunused, t=datetime.datetime.now()).save()

def get_memory_info():
    list = per_memory.query.descending('t').limit(19).all()[::-1]
    values = []
    for value in list:
        values.append(round(value.p))
    return values