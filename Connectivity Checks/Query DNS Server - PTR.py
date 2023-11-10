# Checks DNS connectivity by querying PTR record against domain controller
import dns.resolver
from dns import reversename

dns_server = '10.141.29.22'
lookup_host = dns_server
record_type = 'PTR'
response_timeout = 3

try:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    # set timeout
    resolver.timeout = response_timeout
    resolver.lifetime = response_timeout
    reverse_name = reversename.from_address(dns_server)
    print("Reverse name: %s" % reverse_name)

    try:
        # do DNS lookup
        records = resolver.query(reverse_name, record_type)
        for record in records:
            print(record)
    except dns.resolver.NXDOMAIN:
        print("No such domain exists: %s" % lookup_host)
    except dns.resolver.Timeout:
        print("DNS request to %s has timed out" % lookup_host)
    except dns.exception.DNSException, e:
        print("Exception occurred: %s" % e)
except Exception, e:
    print("Exception occurred: %s" % e)
