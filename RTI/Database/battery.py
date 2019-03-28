from . import db as DB
from RTI.Feature.battery import *

def per_battery_upload(batterypercent, batterystatus):
    collection  = DB.per_battery
    collection.insert({"p": batterypercent, "s": batterystatus})
