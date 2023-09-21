import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

result = re.search(regex, "99 elephants in a [cage]")
print(result[1])

# EN LAS LINEAS 10,11 Y 12 INTENTAMOS ACCEDER AL ÍNDICE 1 DE UNA VARIABLE QUE NO ERA NINGUNO, miralo en el siguiente RESOLVIENDO PID file

