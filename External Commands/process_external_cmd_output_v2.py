#!/usr/bin/python -tt

import subprocess

# Basically, this "pipes" whatever cmd outputs to stdout and stderr to in-memory buffers prepared by subprocess.
# What you do with the content of those buffers are up to you.
# You can examine them, or don't bother with them altogether.
# But the side effect of piping to these buffers is that they won't be printed to the terminal's.
exit_code = subprocess.call(['ping', '-n', '2', '-w', '1000', 'google.com'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

if exit_code == 0:
    print('Success')
else:
    print('Failure')