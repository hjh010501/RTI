import os, platform, subprocess, re
from pymongo import MongoClient
from RTI.loader import feature_load

def sysctl(attr):
    return str(subprocess.check_output(['/usr/sbin/sysctl', "-n", attr]).strip(), "utf-8")


feature_load('battery',
             'cpu',
             'disk',
             'memory')

