import scapy.all as scapy

def packet_callback(packet):
    # Check if the packet has an IP layer (IPv4)
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol_num = packet[scapy.IP].proto

        # Map basic protocol numbers to their names
        protocol_name = "Unknown"
        if protocol_num == 6:
            protocol_name = "TCP"
        elif protocol_num == 17:
            protocol_name = "UDP"
        elif protocol_num == 1:
            protocol_name = "ICMP"

        print(f"\n[*] Packet Captured: {source_ip} --> {destination_ip} | Protocol: {protocol_name}")

        # Check for and extract the payload (Raw data)
        if packet.haslayer(scapy.Raw):
            try:
                # Load the raw payload and decode it if possible
                payload = packet[scapy.Raw].load
                # Print the first 50 characters to keep the output readable
                print(f"    [+] Payload (Raw): {payload[:50]}") 
            except Exception as e:
                print(f"    [-] Could not read payload: {e}")

def start_sniffing(interface=None):
    print(f"[*] Starting Network Sniffer... Press Ctrl+C to stop.")
    # sniff() captures the traffic. 
    # store=False keeps it from holding all packets in memory.
    # prn=packet_callback passes each captured packet to our function.
    scapy.sniff(iface=interface, store=False, prn=packet_callback)

if __name__ == "__main__":
    # You can specify your network interface inside start_sniffing() 
    # e.g., start_sniffing("eth0") or start_sniffing("Wi-Fi")
    # Leaving it empty sniffs on all active interfaces.
    start_sniffing("Ethernet")