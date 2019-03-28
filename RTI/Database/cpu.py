from . import db as DB
from RTI.Feature.cpu import *

def per_cpu_upload(p):
    collection  = DB.per_cpu
    collection.insert({"p": p})

def info_cpu_upload():
    collection = DB.info_cpu
    cpuname = get_processor_name()
    cpucore = get_processor_core()
    cputhread = get_processor_thread()
    collection.insert({"n": cpuname, "c": cpucore, "t": cputhread})

info_cpu_upload()