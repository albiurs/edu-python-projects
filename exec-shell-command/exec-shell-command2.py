#!/usr/bin/env python3

# execute echo command by subprocess.Popen
import subprocess
subprocess = subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)


# execute ls -l by Popen - \n not interpreted as line breaks
import subprocess
subprocess = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)


# execute cmmands using subprocess.call
import subprocess
subprocess.call(['df', '-h'])
subprocess.call(['tail', '-n', '3', '/var/log/kern.log'])
subprocess.call(['ls', '-lah'])
