# Reads a list of hostnames from a .txt file
# Performs forward lookup and reverse DNS lookup
# Records results to a .txt file
#
# If forward lookup is successful, then ipaddress is recorded for "Forward?" column otherwise "NO" is recorded
# If reverse lookup is successful, then hostname is recorded  for "Reverse?" column otherwise "NO" is recorded

import socket

hosts_file = "hosts.txt"
results_file = "results.txt"
fh = open(results_file, "w")
with open(hosts_file, "rU") as rows:
    fh.write("Hostname,Forward?,Reverse?\n")
    for host in rows:
        # init vars
        ip = ''
        hostname = ''
        # strip leading and trailing whitespaces
        host = host.strip()
        fh.write(host)
        # do forward dns lookup
        try:
            ip = socket.gethostbyname(host)
            fh.write("," + ip + ",")
        except socket.error, msg:
            # print "DNS lookup failed for %s: %s" % (host, msg)
            fh.write(",NO,NO\n")
            continue
        # if ip:
            # print "ip: %s" % ip
        # do reverse dns lookup
        try:
            hostname = socket.gethostbyaddr(ip)
            fh.write(hostname[0] + "\n")
        except socket.error, msg:
            # print "Reverse DNS lookup failed for %s: %s" % (ip, msg)
            fh.write("NO\n")
            continue
        # if hostname:
        # print "hostname: %s" % hostname[0]
    # close results file
    fh.close()
