from RTI import app
from RTI.feature.battery import *

@app.route('/battery')
def BatteryUsage():
    return "Battery: " + get_battery_status() + ", " +  get_battery_status('status')