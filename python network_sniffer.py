import scapy.all as scapy

def analyze_traffic(packet):
    if not packet.haslayer(scapy.IP):
        return

    ip_layer = packet[scapy.IP]
    
    proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    proto = proto_map.get(ip_layer.proto, str(ip_layer.proto))

    print(f"Captured => SRC: {ip_layer.src:<15} | DST: {ip_layer.dst:<15} | PROTO: {proto}")

    if packet.haslayer(scapy.Raw):
        payload_data = packet[scapy.Raw].load
        decoded_chunk = payload_data[:50].decode('utf-8', errors='ignore').strip()
        if decoded_chunk:
            print(f"   [Data Snippet]: {decoded_chunk}")

def initiate_sniffing(target_iface: str):
    print(f"Listening on {target_iface}... (Ctrl+C to abort)")
    scapy.sniff(iface=target_iface, store=False, prn=analyze_traffic)

if __name__ == "__main__":
    initiate_sniffing("Ethernet")
