from . import db as DB
from RTI.Feature.disk import *

class per_disk(DB.Document):
    p = DB.FloatField()
    used = DB.FloatField()
    unused = DB.FloatField()
    s = DB.FloatField()

def per_disk_upload(diskpercent, diskused, diskunused, disksize):
    per_disk(p=diskpercent, used=diskused, unused=diskunused, s=disksize).save()
