from . import db as DB
from RTI.Feature.cpu import *

def per_cpu_upload():
    collection  = DB.per_cpu
    cpu_per = get_processor_usage('percent')
    collection.insert({"p": cpu_per})

def info_cpu_upload():
    collection = DB.info_cpu
    cpuname = get_processor_name()
    cpucore = get_processor_core()
    cputhread = get_processor_thread()
    collection.insert({"n": cpuname, "c": cpucore, "t": cputhread})

per_cpu_upload()
info_cpu_upload()