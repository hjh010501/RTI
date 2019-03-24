from RTI import app
from RTI.Feature.cpu import *

@app.route('/cpu')
def CPUUsage():
    return "CPU Name: " + get_processor_name() +\
           "<br>Cores: " + get_processor_core() +\
           "<br>Threads: " + get_processor_thread() +\
           "<br>Usage: " + get_processor_usage("percent")