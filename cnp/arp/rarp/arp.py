arp_table = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0b:22:44:55:66",
    "192.168.1.3": "00:0c:33:77:88:99",
    "192.168.1.4": "00:0d:44:aa:bb:cc"
}

def find_mac_address(ip_address):
    if ip_address in arp_table:
        print(f'IP Address: {ip_address} --> MAC Address: {arp_table[ip_address]}')
    else:
        print(f'IP Address: {ip_address} is not found')

if __name__ == "__main__":
    ip_address = input("Enter IP Address to resolve: ").strip()
    find_mac_address(ip_address)
