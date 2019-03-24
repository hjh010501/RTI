from . import db as DB
from RTI.Feature.disk import *

def per_disk_upload():
    collection  = DB.per_disk
    diskused = get_disk_status('used')
    diskunused = get_disk_status('unused')
    disksize = get_disk_status('size')
    diskpercent = get_disk_status('percent')
    collection.insert({"p": diskpercent, "used": diskused, "unused": diskunused, "s": disksize})

per_disk_upload()