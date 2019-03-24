from RTI.Feature import *
import shlex


def get_battery_status(type='percent'):
    battery = " ".join(str(subprocess.check_output(['pmset', '-g', 'batt']).strip(), "utf-8")).replace(" ", "").replace("\n", ";").replace("\t",";").split(";")
    if type=='percent':
        return int(battery[2].replace("%", ""))
    elif type=='status':
        return battery[3]