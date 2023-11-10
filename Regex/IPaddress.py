import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
ripv2StaticRoutes = [{'gwIpAddress': '68.0.1.1','subnetMask': '255.255.255.0','netIpAddress': '68.0.1.0'},{'gwIpAddress': '78.0.1.1', 'subnetMask': '255.255.255.0','netIpAddress': '78.0.1.0'}]

def check_ipaddr(ip):
    if (re.search(regex, ip)):
        return 1
    else:
        return 0

def check_ripv2_routes(routes):
    try:
        if routes is None or str(routes) == "" or str(routes).isspace():
            return 'Routes cannot be empty'
        for rt in routes:
            print('>>> Processing route ' + str(rt))
            for key, value in rt.items():
                print('Validating key: ' + str(key) + ' ...')
                if key not in ['gwIpAddress', 'netIpAddress', 'subnetMask']:
                    return 'Invalid Ripv2 route key: ' + str(key)
                print('Validating ip: ' + str(value) + ' ...')
                if not check_ipaddr(value):
                    return 'Invalid IPaddress ' +  str(value) + ' for RIPv2 key: ' + str(key)
                print('Processed ip: ' + str(value) + '; Return value: ' + str(check_ipaddr(value)))
            print('<<< Processed route ' + str(rt))
        print('All routes processed')
        return 1
    except Exception as e:
        return 'Exception encountered: ' + str(e)


ret_val = check_ripv2_routes(ripv2StaticRoutes)

if ret_val == 1:
    print('validation succeeded')
else:
    print('ERR: ' + ret_val)