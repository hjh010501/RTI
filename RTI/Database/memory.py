from . import db as DB
from RTI.Feature.memory import *


class per_memory(DB.Document):
    p = DB.FloatField()
    used = DB.IntField()
    unused = DB.IntField()

def per_memory_upload(memoryused, memoryunused, memorypercent):
    per_memory(p=memorypercent, used=memoryused, unused=memoryunused).save()