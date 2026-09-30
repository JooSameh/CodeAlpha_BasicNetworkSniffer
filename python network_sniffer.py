import scapy.all as scapy

def analyze_traffic(packet):
    """
    Callback function to process intercepted packets.
    Kept lightweight intentionally to prevent packet dropping during high-volume traffic.
    """
    if not packet.haslayer(scapy.IP):
        return

    ip_layer = packet[scapy.IP]
    
    # Map common protocols; fallback to raw string representation if unmapped (e.g., OSPF, IGMP)
    proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    proto = proto_map.get(ip_layer.proto, str(ip_layer.proto))

    print(f"Captured => SRC: {ip_layer.src:<15} | DST: {ip_layer.dst:<15} | PROTO: {proto}")

    if packet.haslayer(scapy.Raw):
        payload_data = packet[scapy.Raw].load
        # Safe decode: ignore errors to prevent crashes on encrypted or malformed binary payloads
        decoded_chunk = payload_data[:50].decode('utf-8', errors='ignore').strip()
        if decoded_chunk:
            print(f"   [Data Snippet]: {decoded_chunk}")

def initiate_sniffing(target_ifaces):
    """Initializes the sniffer in stateless mode (store=False) to avoid memory leaks."""
    print(f"Listening on {target_ifaces}... (Ctrl+C to abort)")
    scapy.sniff(iface=target_ifaces, store=False, prn=analyze_traffic)

if __name__ == "__main__":
    # Bind to primary active NICs
    initiate_sniffing(["Ethernet", "Wi-Fi"])
