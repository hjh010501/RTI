import RTI.Resource.cpu
import RTI.Resource.memory
import RTI.Resource.disk
import RTI.Resource.battery
from RTI import app

from RTI.Feature.cpu import *
from RTI.Feature.memory import *

@app.route('/')
def ALLInfo():
    return  "CPU Name: " + get_processor_name() +\
           "<br>Cores: " + get_processor_core() +\
           "<br>Threads: " + get_processor_thread() +\
           "<br>Usage: " + get_processor_usage("percent") +\
           "<br>Usage: " + get_memory_usage('percent') +\
           "<br>Unused memory: " + get_memory_usage("unused") + "MB" +\
           "<br>Used memory: " + get_memory_usage("used") + "MB"