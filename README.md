# CodeAlpha_BasicNetworkSniffer

## Overview
So, I built this python sniffer for my first CodeAlpha internship task. It relies on the scapy module to grab network packets while they are moving. Basically, it looks at the traffic and dumps out the IPs (source and dest), tells you the protocol, and tries to grab some payload text if there is any.

## What it does
- Sniffs the local network live.
- Identifies if we are looking at TCP, UDP or just ICMP pings.
- Dumps a tiny piece of the raw data.

## Requirements
Before running it, make sure you got:
- Python 3 setup.
- The scapy package (run `pip install scapy` in cmd).
- Important: Windows users must get Npcap installed first. The script will fail without it.

## Usage
Just run the script from your terminal. Make sure you open cmd as admin, or use sudo on linux, because packet grabbing needs root access.
Run: `python network_sniffer.py`

*Quick Tip:* Need to target a specific card like your Wi-Fi? Just edit the interface string at the very bottom of the python file.

## Disclaimer 
This was made for my training tasks only. Do not use this to snoop on networks that are not yours.
