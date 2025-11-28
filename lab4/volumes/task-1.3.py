#!/usr/bin/env python3
from scapy.all import *

hostname = "google.com"
# hostname = "cs.unc.edu"

#TODO
# Modify the upper_bound variable so that 
# you can see how many routers there are 
# from you to your destination.

upper_bound = 50

for i in range(1, upper_bound):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    reply = sr1(pkt, verbose=0, timeout=3)
    if reply == None:
        break
    elif reply.type == 3:
        print("Done", reply.src)
        break
    else:
        print("%d hops away: " % i, reply.src)
print("Traceroute complete")
