import dis
"""
The dis module supports the analysis of CPython bytecode by disassembling it.
"""
count = 0

def increment():
    global count
    count += 1

# prints the bytecode
dis.dis(increment)