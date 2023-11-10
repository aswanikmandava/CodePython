# Reads a list of hostnames or ipaddresses from a .txt file
# Performs a TCP port check to see if the port is open
# Records results to a .txt file
#
# If port is open, "YES" is recorded in results_file for "Open?" column
# If an exception occurs, "ERROR" is recorded

import socket

# init vars
hosts_file = "hosts.txt"
results_file = "results.txt"
# TCP port to check
port = 22

fh = open(results_file, "w")
with open(hosts_file, "rU") as rows:
    fh.write("Hostname,Open?\n")
    for host in rows:
        # strip leading and trailing whitespaces
        host = host.strip()
        fh.write(host)

        # Open a socket
        sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set socket timeout to 1 sec
        sock_obj.settimeout(1)

        try:
            # Connect to remote server port
            sock_obj.connect((host, port))
            # stop sending and receiving on this connection
			sock_obj.shutdown(socket.SHUT_RDWR)
            # release connection resources
			sock_obj.close()
            print "Port %s is open on %s" %(port, host)
            fh.write(",YES\n")
        except socket.error, msg:
            print "Socket error on %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue
        except Exception as e:
            print "Socket exception on %s: %s" % (host, e)
            fh.write(",ERROR\n")
            continue

    # End of for loop 
    # close results file
    fh.close()
