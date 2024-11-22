# Reads a list of hostnames or ipaddresses from a .txt file
# Performs a ping check to see if the host is reachable
# Records results to a .txt file
#
# If host is online, "YES" is recorded in results_file for "Ping?" column
# If host is offline or unreachable, "NO" is recorded
# If an exception occurs, "ERROR" is recorded 

import sys
import subprocess

hosts_file = "hosts.txt"
results_file = "results.txt"
fh = open(results_file, "w")
with open(hosts_file, "rU") as rows:
    fh.write("Host,Ping?\n")
    for host in rows:
        # strip leading and trailing whitespaces
        host = host.strip()
        fh.write(host)
        try:
            # send 1 icmp packet with 1 sec as timeout	
            ping_cmd = ['ping', '-c', '1', '-W', '1', host]
            # Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.
            ping_obj = subprocess.Popen(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
            # Uncomment below lines to see ping output

            #with ping_obj.stdout:
            #    for line in iter(ping_obj.stdout.readline, b''):
            #       print line

            # Wait for process to terminate. 
            # Return code:
            #    0 - Success
            #    1 - Failure (Unreachable host)
            ping_status = ping_obj.wait()
 
            # print "Ping result: %d" %ping_status
            if ping_status == 0:
                fh.write(",YES\n")
            else:
                fh.write(",NO\n")	
        except subprocess.CalledProcessError, msg:
            # print "Exception for %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue
        except OSError, msg:
            # print "Exception - OSError for %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue
        except Exception, msg:
            # print "Exception for %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue
		
    # close results file
    fh.close()
