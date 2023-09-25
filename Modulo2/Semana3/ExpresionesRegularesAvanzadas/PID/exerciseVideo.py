import re

def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s+([A-Z]+)(?:\s+([A-Z][a-z]+))*\s+(.+)$"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result.group(1), result.group(2))

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

"""Se necesita una expresión regular más precisa para capturar el mensaje que sigue al PID. Esta expresión regular utiliza
grupos de captura adicionales para garantizar que el mensaje esté correctamente capturado después del estado en mayúsculas.
El tercer grupo de captura (?:\s+([A-Z][a-z]+))* se encarga de capturar palabras adicionales después del estado en mayúsculas
(si las hay) antes de llegar al mensaje principal. Luego, en la función format, utilizamos result.group(1) para obtener el PID
y result.group(2) para obtener el estado en mayúsculas."""
