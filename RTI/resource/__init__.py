from RTI.database.cpu import get_cpu_info
from RTI.database.memory import get_memory_info
from RTI.database.disk import get_disk_info
from RTI.database.battery import get_battery_info
from RTI import app

from RTI.feature.cpu import *
from RTI.feature.memory import *

from flask import render_template, send_from_directory, request

dbinfo = {
    'cpu_info': get_processor_name() + ", " + get_processor_thread() + " Threads",
    'cpu': get_cpu_info(),
    'memory': get_memory_info(),
    'disk': get_disk_info(),
    'battery': get_battery_info()
}

@app.route('/')
def ALLInfo():
       return render_template('index.html', dbinfo=dbinfo)
