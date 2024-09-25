def validate_ip(ip):
    octets = ip.split('.')
    
    if len(octets) != 4:
        return False
    
    for octet in octets:
        try:
            value = int(octet)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False
    
    return True

def validate_subnet_mask(subnet_mask):
    octets = subnet_mask.split('.')
    if len(octets) != 4:
        return False
    
    for octet in octets:
        try:
            value = int(octet)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False
    
    return True

def calculate_network_details(ip, subnet_mask):
    
    ip_parts = list(map(int, ip.split('.')))
    mask_parts = list(map(int, subnet_mask.split('.')))
    
    #### Calculate network ID
    network_id = [ip_parts[i] & mask_parts[i] for i in range(4)]
    
    #### Calculate broadcast ID
    broadcast_id = [network_id[i] | (255 - mask_parts[i]) for i in range(4)]
    
    #### Calculate first usable IP (network ID + 1)
    first_usable_ip = network_id[:]
    first_usable_ip[3] += 1
    
    #### Calculate last usable IP (broadcast ID - 1)
    last_usable_ip = broadcast_id[:]
    last_usable_ip[3] -= 1
    
    #### Calculate total number of hosts
    total_hosts = (2 ** (32 - sum(bin(x).count('1') for x in mask_parts))) 
    usable_hosts = total_hosts - 2
    
    return {
        "network_range": f"{first_usable_ip[0]}.{first_usable_ip[1]}.{first_usable_ip[2]}.{first_usable_ip[3]} - {last_usable_ip[0]}.{last_usable_ip[1]}.{last_usable_ip[2]}.{last_usable_ip[3]}",
        "network_id": f"{network_id[0]}.{network_id[1]}.{network_id[2]}.{network_id[3]}",
        "broadcast_id": f"{broadcast_id[0]}.{broadcast_id[1]}.{broadcast_id[2]}.{broadcast_id[3]}",
        "default_gateway": f"{network_id[0]}.{network_id[1]}.{network_id[2]}.{network_id[3]+1}",
        "total_hosts": total_hosts,
        "usable_hosts": usable_hosts
    }

def user_input():
    while True:
        #### user ip address 
        user_ip = input("Enter your IP address: ")
        if not validate_ip(user_ip):
            print("ERROR: Invalid IP address. Please try again.")
            continue
        
        #### subnet mask 
        subnet_mask = input("Enter your subnet mask: ")
        if not validate_subnet_mask(subnet_mask):
            print("ERROR: Invalid subnet mask. Please try again.")
            continue
        
        print("Both IP address and subnet mask are valid!")
        
        # Calculate and display network details
        details = calculate_network_details(user_ip, subnet_mask)
        
        print("\n--- Network Details ---")
        print(f"Network Range: {details['network_range']}")
        print(f"Network ID: {details['network_id']}")
        print(f"Broadcast ID: {details['broadcast_id']}")
        print(f"Default Gateway: {details['default_gateway']}")
        print(f"Total Number of Hosts: {details['total_hosts']}")
        print(f"Number of Usable Hosts: {details['usable_hosts']}")
        print()
        break

def main():
    user_input()

if __name__ == "__main__":
    main()