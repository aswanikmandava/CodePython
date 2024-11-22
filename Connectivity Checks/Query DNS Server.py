# Check DNS connection by querying A record against domain controller
import dns.resolver

dns_server = '10.141.29.22'
lookup_host = 'pspwvi-ctwadf02.sts.nycnet'
record_type = 'A'
response_timeout = 3

try:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    # set timeout
    resolver.timeout = response_timeout
    resolver.lifetime = response_timeout

    try:
        # do DNS lookup
        records = resolver.query(lookup_host, record_type)
        for record in records:
            print(record)
    except dns.resolver.NXDOMAIN:
        print("No such domain exists: %s" % lookup_host)
    except dns.resolver.Timeout:
        print("DNS request to %s has timed out" % lookup_host)
    except dns.exception.DNSException as e:
        print("Exception occurred: %s" % e)
except Exception as e:
    print("Exception occurred: %s" % e)