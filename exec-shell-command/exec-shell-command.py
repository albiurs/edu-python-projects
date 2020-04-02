#!/usr/bin/env python3

import os, subprocess

# using os class
def executeShellCommand(cmd):
    return os.system(cmd)

print("os: " + str(executeShellCommand('tail -n 1 /var/log/kern.log'))


# using subprocess class
subprocess.Popen(["tail","-1", "/var/log/kern.log"])
output = subprocess.check_output(["tail","-1", "/var/log/kern.log"])
print("check output: " + str(output))
