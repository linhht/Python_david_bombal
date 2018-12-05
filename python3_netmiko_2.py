from netmiko import ConnectHandler

sw_1 = {
    'device_type': 'cisco_ios',
    'ip': '1.1.1.11',
    'username': 'test',
    'password': 'cisco',
}
sw_2 = {
    'device_type': 'cisco_ios',
    'ip': '1.1.1.22',
    'username': 'test',
    'password': 'cisco',
}

with open('sw_cmd') as f:
    lines = f.read().splitlines()
print(lines)

all_dev = [sw_1, sw_2]

for dev in all_dev:
    net_connect = ConnectHandler(**dev)
    for n in range (100,102):
        print('Create vlan '+str(n))
        config_cmd = ['vlan '+str(n)]
        output = net_connect.send_config_set(config_cmd)
        print(output)
    output = net_connect.send_config_set(lines)
    print(output)
