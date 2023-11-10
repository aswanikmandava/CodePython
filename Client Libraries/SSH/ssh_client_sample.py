"""
The following example shows two ways of opening an SSH connection to example.com. 
The first function sets the missing host key policy to AutoAddPolicy. 
If the host key verification fails, the client will continue to interact with the server, even though the connection 
may be compromised. The second function sets the host key policy to RejectPolicy, and will throw an exception if the 
host key verification fails.
"""
from paramiko.client import SSHClient, AutoAddPolicy, RejectPolicy
from paramiko import SSHException

def unsafe_connect():
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    client.connect("example.com")
    # ... interaction with server
    command = 'hostname'
    try:
        # execute a command on remote host which returns handles to I/O streams
        stdin_, stdout_, stderr_ = client.exec_command(command)
        # get command exit status
        exit_status_ = stdout_.channel.recv_exit_status()
        # get command output
        result = stdout_.readlines()
        for line in result:
            print(line)
    except SSHException:
        pass
    finally:
        client.close()

def safe_connect():
    client = SSHClient()
    client.set_missing_host_key_policy(RejectPolicy)
    client.connect("example.com")

    # ... interaction with server

    client.close()