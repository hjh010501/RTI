from RTI.feature import *
import shlex

def get_processor_name():
    return sysctl("machdep.cpu.brand_string")


def get_processor_core():
    return sysctl("machdep.cpu.core_count")


def get_processor_thread():
    return sysctl("machdep.cpu.thread_count")


def get_processor_usage(type='all'):
    process = subprocess.Popen("top", stdout=subprocess.PIPE)
    while True:
        output = process.stdout.read(process.stdout.__sizeof__())
        if output == '' and process.poll() is not None:
            break
        if output:
            result = str(output).split('\\n')[3]
            if type=='percent':
                return float(result.replace("CPU usage: ", "")[:result.replace("CPU usage: ", "").find("user")].replace("%", "").replace(" ", ""))
            elif type=='all':
                return result