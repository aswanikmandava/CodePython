# Reads a list of hostnames or ipaddresses from a .txt file
# Performs a ping check to see if the host is reachable
# Records results to a .txt file
#
# If host is online, "YES" is recorded in results_file for "Ping?" column
# If host is offline or unreachable, "NO" is recorded
# If an exception occurs, "ERROR" is recorded 

import sys
import re
import subprocess


def ping_host(host, fh):
    host = host.strip()
    fh.write(f"{host},")
    # send 1 icmp packet with 1 sec as timeout
    ping_cmd = ['ping', '-n', '1', '-w', '1', host]
    # Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.
    ping_obj = subprocess.Popen(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Uncomment below lines to see ping output
    output = []
    with ping_obj.stdout:
        output = ping_obj.stdout.readlines()
        # for line in iter(ping_obj.stdout.readline, b''):
        #     output.append(line)
        #
        out_string = b",".join(output)
        print(out_string)
    #         print(line)

    # Wait for process to terminate.
    # Return code:
    #    0 - Success
    #    1 - Failure (Unreachable host)
    ping_status = ping_obj.wait()
    # print "Ping result: %d" %ping_status
    # if ping_status == 0:
    #     fh.write("YES")
    # else:
    #     fh.write("NO")
    if re.search('.*Reply from.*', str(out_string)):
        fh.write("YES")
    else:
        fh.write("NO")



hosts_file = "hosts.txt"
results_file = "results.txt"
fh = open(results_file, "w")
with open(hosts_file, "r") as rows:
    fh.write("Hostname,Mgmt_IP,Ping?,Srv_IP,Ping?\n")
    for row  in rows:
        hostname, mgmt_ip, service_ip = row.split(',')
        # strip leading and trailing whitespaces
        # print(f"mgmt: {mgmt_ip}, srv_ip: {service_ip}")

        try:
            fh.write(f"{hostname},")
            ping_host(mgmt_ip, fh)
            fh.write(",")
            ping_host(service_ip, fh)
            fh.write("\n")
        except subprocess.CalledProcessError as msg:
            # print "Exception for %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue
        except OSError as msg:
            # print "Exception - OSError for %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue
        except Exception as msg:
            # print "Exception for %s: %s" % (host, msg)
            fh.write(",ERROR\n")
            continue