# for index in range(1,6):
#     print("index: {}".format(index))

route_index_map = {"1":"no", "2":"no", "3": "yes", "4": "yes", "5":"no"}

# print(list(route_index_map.values()).index('no')+1)

ripv2_routes = [{"gwIp": "1.2.2.3", "nwIp": "1.2.2.0", "mask": "255.255.255.0"},
              {"gwIp": "2.2.2.3", "nwIp": "2.2.2.0", "mask": "255.255.255.0"},
              {"gwIp": "3.2.2.3", "nwIp": "3.2.2.0", "mask": "255.255.240.0"}]

ripv2_routes.pop(1)

print(ripv2_routes)
