rarp_table = {
    "00:0a:95:9d:68:16": 
        "192.168.1.1",
    "00:0b:22:44:55:66": 
        "192.168.1.2",
    "00:0c:33:77:88:99": 
        "192.168.1.3",
    "00:0d:44:aa:bb:cc": 
        "192.168.1.4"
}

def find_ip_address(mac_address):
    if mac_address in rarp_table:
        print(f'Mac Address:{mac_address}--> IP Address:{rarp_table[mac_address]}')
    else:
        print(f'Mac Address:{mac_address} is not found')

if __name__ == "__main__":
    mac_address = input("Enter MAC Address to resolve: ").strip()
    find_ip_address(mac_address)
