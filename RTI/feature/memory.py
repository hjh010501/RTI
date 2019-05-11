from RTI.feature import *
import shlex


def get_memory_usage(type='all'):
    process = subprocess.Popen("top", stdout=subprocess.PIPE)
    while True:
        output = process.stdout.read(process.stdout.__sizeof__())
        if output == '' and process.poll() is not None:
            break
        if output:
            result = str(output).split('\\n')[6]

            used = result.replace("PhysMem: ", "")[:result.replace("PhysMem: ", "").find(' used')].find("G")\
                   is not -1 and \
                   int(result.replace("PhysMem: ", "")[:result.replace("PhysMem: ", "").find(' used')].replace("G","")) * 1024\
                   or int(result.replace("PhysMem: ", "")[:result.replace("PhysMem: ", "").find(' used')].replace("M",""))


            unused = result.replace("PhysMem: ", "")[result.replace("PhysMem: ", "").find(', ')+2:result.replace("PhysMem: ", "").find(' unused')].find('G') is not -1 and \
            int(result.replace("PhysMem: ", "")[result.replace("PhysMem: ", "").find(', ') + 2:result.replace("PhysMem: ", "").find(' unused')].replace("G", "")) or \
            int(result.replace("PhysMem: ", "")[result.replace("PhysMem: ", "").find(', ')+2:result.replace("PhysMem: ", "").find(' unused')].replace("M",""))

            if type=='all':
                return result
            elif type=='used':
                return used
            elif type=='unused':
                return unused
            elif type=='percent':
                size = used + unused
                used = size - unused
                return float(round(used / size * 100, 2))