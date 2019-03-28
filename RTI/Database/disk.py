from . import db as DB
from RTI.Feature.disk import *

def per_disk_upload(diskpercent, diskused, diskunused, disksize):
    collection  = DB.per_disk
    collection.insert({"p": diskpercent, "used": diskused, "unused": diskunused, "s": disksize})
