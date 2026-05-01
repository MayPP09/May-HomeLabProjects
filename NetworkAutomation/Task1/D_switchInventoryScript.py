from netmiko import ConnectHandler

switch_list = [
    {'device_type': 'extreme_exos', 'host': '10.10.1.24', 'username': 'admin', 'password': ''},
    {'device_type': 'extreme_exos', 'host': '10.10.1.23', 'username': 'admin', 'password': ''},
    {'device_type': 'extreme_exos', 'host': '10.10.1.22', 'username': 'admin', 'password': ''},
    {'device_type': 'extreme_exos', 'host': '10.10.1.21', 'username': 'admin', 'password': ''}
]
with open('D_switch_configurations.txt', 'w') as f:
    for switch in switch_list:
        print(f"Connecting to {switch['host']}...")
        
        # Connect to the switch
        net_connect = ConnectHandler(**switch)
        
        # Get the switch name and basic info
        switch_data = net_connect.send_command('show switch')
        
        # Get the configuration (requested ~20 lines)
        config_data = net_connect.send_command('show configuration')
        
        # Format the data for the inventory file
        output = f"Switch IP: {switch['host']}\n"
        output += f"{switch_data}\n"
        output += "--- Configuration Data ---\n"
        output += f"{config_data[:1000]}\n" # Takes approximately the first 20 lines
        output += "="*30 + "\n"
        
        # Write to file and print to screen for your screenshot
        f.write(output)
        print(output)
        
        net_connect.disconnect()