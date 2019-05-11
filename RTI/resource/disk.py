from RTI import app
from RTI.feature.disk import *

@app.route('/disk')
def DiskUsage():
    return "Used: " + str(round(int(get_disk_status('used')) / 1000, 1)) + "GB" +\
           "<br> Unused: " + str(round(int(get_disk_status('unused')) / 1000, 1)) + "GB" +\
           "<br> Size: " + str(round(int(get_disk_status('size')) / 1000, 1)) + "GB" +\
           "<br> Percent: " + str(get_disk_status('percent')) + "%"