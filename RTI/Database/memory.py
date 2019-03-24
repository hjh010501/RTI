from . import db as DB
from RTI.Feature.memory import *

def per_memory_upload():
    collection  = DB.per_memory
    memoryused = get_memory_usage('used')
    memoryunused = get_memory_usage('unused')
    memorypercent = get_memory_usage('percent')
    collection.insert({"p": memorypercent, "used": memoryused, "unused": memoryunused})

per_memory_upload()