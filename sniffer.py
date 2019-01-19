import socket, sys, time
from struct import *

try:
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error, msg :
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

counters = {"eth": 0, "ip": 0, "icmp_ip": 0, "tcp_ip": 0, "udp_ip": 0}
oldtime=time.time()
while True:
    packet = s.recvfrom(65565)
    packet = packet[0]
    counters['eth']+=1
    eth_length = 14 
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    #IP = 8
    if eth_protocol == 8 :
	counters['ip']+=1
        ip_header = packet[eth_length:20+eth_length]
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
        protocol = iph[6]
        if protocol == 1 :
            counters['icmp_ip']+=1
        elif protocol == 6 :
            counters['tcp_ip']+=1
        elif protocol == 17 :
            counters['udp_ip']+=1
    if(time.time() - oldtime > 3) :
        print 'All packets {}: IP packets {} incl. ICMP {}, TCP {}, UDP {}'.format(counters['eth'], counters['ip'], counters['icmp_ip'], counters['tcp_ip'], counters['udp_ip'])
        oldtime = time.time()

