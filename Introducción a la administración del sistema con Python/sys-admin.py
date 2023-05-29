import os
import subprocess

# Listar archivos y directorios en el directorio actual
os.system("dir")

# Listar archivos y directorios en el directorio actual utilizando subprocess
subprocess.run(["dir"], shell=True)

# Listar archivos y directorios en formato detallado
subprocess.run(["dir", "/w"])

# Obtener información del sistema
command = "systeminfo"
subprocess.run([command])

# Obtener información de los procesos en ejecución
command = "tasklist"
subprocess.run([command])

"""import os
import subprocess
os.system("ls")

subprocess.run(["ls"])

subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])"""
