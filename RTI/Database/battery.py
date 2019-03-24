from . import db as DB
from RTI.Feature.battery import *

def per_battery_upload():
    collection  = DB.per_battery
    batterypercent = get_battery_status('percent')
    batterystatus = get_battery_status('status')
    collection.insert({"p": batterypercent, "s": batterystatus})

per_battery_upload()