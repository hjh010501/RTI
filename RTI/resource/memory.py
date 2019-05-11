from RTI import app
from RTI.feature.memory import *

@app.route('/memory')
def MemoryUsage():
    return "Usage: " + str(get_memory_usage('percent')) + "%" +\
           "<br>Unused memory: " + str(get_memory_usage("unused")) + "MB" +\
           "<br>Used memory: " + str(get_memory_usage("used")) + "MB"