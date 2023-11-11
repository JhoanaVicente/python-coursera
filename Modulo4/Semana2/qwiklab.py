#!/usr/bin/env python3
# Este script de Python utiliza el módulo multiprocessing para realizar copias de seguridad de los directorios encontrados
# en src utilizando rsync


from multiprocessing import Pool
import os
import subprocess
# Aquí estamos importando los módulos necesarios. multiprocessing se utiliza para realizar operaciones en paralelo, os para
# operaciones relacionadas con el sistema operativo y subprocess para ejecutar comandos en el sistema operativo desde el script.



src = "/home/student-02-abbe9d437a45/data/prod"
dirs = next(os.walk(src))[1]
# Estas líneas definen la ruta de origen (src) y obtienen una lista de todos los directorios en src.



def backingup(dirs):
  dest = "/home/student-02-abbe9d437a45/data/prod_backup"
  subprocess.call(["rsync", "-arq", src+'/'+dirs, dest])

# Esta función toma un directorio como argumento y utiliza rsync para realizar la copia de seguridad de ese directorio
# desde src a un directorio de destino dest



p = Pool(len(dirs))
# Creación de un Pool de Procesos: Aquí creamos un grupo de procesos con la misma cantidad de procesos que directorios.

p.map(backingup, dirs)
# Mapeo de la Función sobre los Directorios: Utilizamos map para aplicar la función backingup a cada directorio en paralelo


"""En resumen, este script realiza copias de seguridad de todos los directorios encontrados en src en paralelo utilizando rsync
para optimizar el proceso. Solo resta ejecutarlo y verificar si funciona correctamente."""
