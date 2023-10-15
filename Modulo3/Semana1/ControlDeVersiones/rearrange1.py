import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .])*$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])
print()




import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everything ok")
