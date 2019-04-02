from . import db as DB
from RTI.Feature.cpu import *

class info_cpu(DB.Document):
    n = DB.StringField()
    c = DB.StringField()
    t = DB.StringField()

class per_cpu(DB.Document):
    n = DB.FloatField()

def per_cpu_upload(p):
    per_cpu(n=p).save()

def info_cpu_upload():
    cpuname = get_processor_name()
    cpucore = get_processor_core()
    cputhread = get_processor_thread()
    info = info_cpu(n=cpuname, c=cpucore, t=cputhread)
    info.save()

info_cpu_upload()