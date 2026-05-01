from netmiko import ConnectHandler

switch_ips = ['10.10.1.24', '10.10.1.23', '10.10.1.22', '10.10.1.21']

output = ""

for ip in switch_ips:
    print(f"Connecting to {ip}...")
    
    device = {
        'device_type': 'extreme_exos',
        'host': ip,
        'username': 'admin',
        'password': '',
    }
    
    # Connect and get VLANs
    connection = ConnectHandler(**device)
    result = connection.send_command('show vlan')
    
    # Format output for the report
    header = f"\n{'='*20}\nSWITCH: {ip}\n{'='*20}\n"
    print(header + result)
    output += header + result
    
    connection.disconnect()

with open('E1_existingVLAN.txt', 'w') as f:
    f.write(output)
