from scapy.all import *
IFACE = "br-ee523bfac14a"

def spoof_reply(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:
        print(f"Original packet detected: {pkt[IP].src} -> {pkt[IP].dst}")
        ip_layer = IP()
        ip_layer.src = pkt[IP].dst
        ip_layer.dst = pkt[IP].src

        icmp_layer = ICMP()
        icmp_layer.type = 0
        icmp_layer.id = pkt[ICMP].id
        icmp_layer.seq = pkt[ICMP].seq

        if Raw in pkt:
            payload = pkt[Raw].load
            reply_pkt = ip_layer/icmp_layer/payload
        else:
            reply_pkt = ip_layer/icmp_layer

        send(reply_pkt, iface = IFACE, verbose = 0)
        print(f"Spoofed reply sent: {reply_pkt[IP].src} -> {reply_pkt[IP].dst}\n")

print(f"Starting sniffer on {IFACE}...")
pkt = sniff(iface=IFACE, filter="icmp[icmptype]==icmp-echo", prn=spoof_reply)
