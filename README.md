# CodeAlpha_BasicNetworkSniffer

## 🛡️ Project Overview
This project is a **Basic Network Sniffer** developed in Python using the `scapy` library. It was created as part of the **Cyber Security Internship at CodeAlpha**. The tool captures network traffic packets in real-time, analyzes their structure, and displays essential information such as Source IP, Destination IP, Protocol (TCP/UDP/ICMP), and Payload data.

## ✨ Features
* **Packet Capturing:** Intercepts live network traffic.
* **Protocol Identification:** Recognizes and maps IP protocols (e.g., TCP, UDP, ICMP).
* **Data Extraction:** Extracts and displays raw payload data (if available and unencrypted).
* **Lightweight & Efficient:** Does not store packets in memory, ensuring the script can run continuously without crashing.

## 🛠️ Prerequisites
Before running this script, ensure you have the following installed:

1. **Python 3.x:** Installed on your system.
2. **Scapy Library:** (Run `pip install scapy` in your terminal)
3. **Npcap (For Windows Users Only):** Windows cannot natively capture raw network packets. You must download and install Npcap for the script to work.

## 🚀 How to Run
1. Clone this repository to your local machine.
2. Open your terminal or command prompt as **Administrator (Windows)** or **Root (Linux/macOS)**.
3. Run the script: (Run `python network_sniffer.py` in your terminal)
4. *Optional:* To specify a specific network interface, edit the `start_sniffing("Interface_Name")` line in the code (e.g., `"Wi-Fi"` or `"Ethernet"`).

## ⚠️ Legal & Ethical Disclaimer
**Educational Purposes Only:** This tool was created exclusively for educational purposes as part of a cybersecurity training program.
* **Do not** use this tool on any network where you do not have explicit permission from the network owner.
* Unauthorized packet sniffing is illegal and a violation of privacy.
* The author and CodeAlpha are not responsible for any misuse or damage caused by this program.

CodeAlphaBasicNetworkSniffer 
🛡️ Project Overview This project is a Basic Network Sniffer developed in Python using the scapy library It was created as part of the Cyber Security Internship at CodeAlpha The tool captures network traffic packets in real-time, analyzes their structure, and displays essential information such as Source IP, Destination IP, Protocol , and Payload data 
✨ Features Packet Capturing: Intercepts live network traffic Protocol Identification: Recognizes and maps IP protocols Data Extraction: Extracts and displays raw payload data Lightweight & Efficient: Does not store packets in memory, ensuring the script can run continuously without crashing 
🛠️ Prerequisites Before running this script, ensure you have the following installed: 1 Python 3.x: Installed on your system 2 Scapy Library: 3 Npcap : Windows cannot natively capture raw network packets You must download and install Npcap for the script to work 
🚀 How to Run 1 Clone this repository to your local machine 2 Open your terminal or command prompt as Administrator or Root 3 Run the script: 4 Optional: To specify a specific network interface, edit the startsniffing line in the code ⚠️ Legal & Ethical Disclaimer Educational Purposes Only: This tool was created exclusively for educational purposes as part of a cybersecurity training program Do not use this tool on any network where you do not have explicit permission from the network owner Unauthorized packet sniffing is illegal and a violation of privacy The author and CodeAlpha are not responsible for any misuse or damage caused by this program
