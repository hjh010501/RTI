from . import db as DB
from RTI.Feature.memory import *

def per_memory_upload(memoryused, memoryunused, memorypercent):
    collection  = DB.per_memory
    collection.insert({"p": memorypercent, "used": memoryused, "unused": memoryunused})