from netmiko import ConnectHandler


switch_ips = ['10.10.1.24', '10.10.1.23', '10.10.1.22', '10.10.1.21']

# create VLANs 
vlan_commands = [
    'create vlan User_Network',
    'configure vlan User_Network tag 10',
    'create vlan ACCT_Network',
    'configure vlan ACCT_Network tag 20',
    'create vlan MGMT_Network',
    'configure vlan MGMT_Network tag 30',
    'create vlan IT_Network',
    'configure vlan IT_Network tag 40'
]

# apply configuration on each switch
for ip in switch_ips:
    print(f"Configuring switch at {ip}...")
    
    device = {
        'device_type': 'extreme_exos',
        'host': ip,
        'username': 'admin',
        'password': '',
    }
    
    # Connect and send the list of commands
    connection = ConnectHandler(**device)
    output = connection.send_config_set(vlan_commands)
    print(output)
    
    with open('E2_createVLAN.txt', 'a') as f:
        f.write(f"Results for Switch {ip}:\n{output}\n\n")
    
    connection.disconnect()