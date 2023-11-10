#!/usr/bin/python -tt

import subprocess
# cmd = 'snmpwalk -v2c -c public localhost system'
# out = subprocess.Popen(['snmpwalk', '-v2c', '-c', 'public', 'localhost', 'system'],
#       stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Basically, this "pipes" whatever cmd outputs to stdout and stderr to in-memory buffers prepared by subprocess.
# What you do with the content of those buffers are up to you.
# You can examine them, or don't bother with them altogether.
# But the side effect of piping to these buffers is that they won't be printed to the terminal's.
out = subprocess.Popen(['ping', '-n', '2', '-w', '1000', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = out.communicate()
# find the exit code
exit_code = out.returncode

if exit_code == 0:
    print('Success')
else:
    print('Failure')

# To print command output, uncomment following lines
lines = stdout.split('\n')
print(type(lines))
for row in lines:
 print row