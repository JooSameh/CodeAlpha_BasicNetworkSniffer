# CodeAlpha Basic Network Sniffer

A lightweight, Scapy-based network packet sniffer developed for the CodeAlpha Cybersecurity Internship (Task 1). 

The script performs real-time traffic interception to extract foundational routing metrics (Source/Destination IPs, Protocols) and raw payload snippets. It uses a stateless callback approach to process packets on the fly, preventing memory bloat during continuous capture.

## Technical Dependencies
- Python 3.8+
- `scapy` 
- Npcap (Strictly required for Windows environments to enable raw socket binding)

## Setup & Execution
1. Install the required package:
   ```bash
   pip install scapy
