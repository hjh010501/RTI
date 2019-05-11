from RTI.feature import *
import shlex


def get_disk_status(type='percent'):
    disk = " ".join(str(subprocess.check_output(['df', '-m']).strip(), "utf-8").split("\n")[1].split()).split(" ")
    if type=="used":
        return float(disk[2])
    elif type=="unused":
        return float(disk[3])
    elif type == "size":
        return float(disk[2]) + float(disk[3])
    elif type == "percent":
        return float(disk[4].replace("%",""))