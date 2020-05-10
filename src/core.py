# -*- coding: utf-8 -*-
from util import getIpAddress,getPort, isSrc
from tcp_packet import tcp_packet
from udp_packet import udp_packet
from rule_engine import rule_engine

def main(f):
    #f = open('../packets/tcp.txt','r')
    while(True):
        f.readline()
        f.readline()
        s = f.readline()
        s = s[6:len(s)-2].split("|")

        #print("Is coming in: ", end='')
        #print(isIncoming(['f8','34','41','21','87','7a'],s[6:12]))

        MACaddress =s[6]+":"+s[7]+":"+s[8]+":"+s[9]+":"+s[10]+":"+s[11] 

        if(s[23]== "06"):
            packet = tcp_packet(MACaddress,\
                         getIpAddress(s[26:30]), \
                         getIpAddress(s[30:34]),\
                         getPort(s[34:36]), \
                         getPort(s[36:38]) )
            



        if(s[23]== "11"):
            packet = udp_packet(MACaddress,\
                         getIpAddress(s[26:30]), \
                         getIpAddress(s[30:34]),\
                         getPort(s[34:36]), \
                         getPort(s[36:38]) )
        print(packet.String())
        f.readline()

        r = rule_engine()
        

        
        #Check if the src of the packet is my device
        #Then the packet is travelling outside my network
        isSuccess = False
        if(isSrc(['f8','34','41','21','87','7a'],s[6:12])):
            print("packet going out of our server..")
            print("source ip:{} and port:{} will {}".format(packet.getSrcIP(),\
                                                                      packet.getSrcPort(),\
                                    r.checkOutboundRules(packet.getSrcIP(), packet.getSrcPort())))
            print("Destination ip:{} and port:{} will {}".format(packet.getDstIP(),\
                                                                      packet.getDstPort(),\
                                    r.checkOutboundRules(packet.getDstIP(), packet.getDstPort())))

            
            isSuccess = r.checkOutboundRules(packet.getSrcIP(), packet.getSrcPort()) == 'Accept' and \
                        r.checkOutboundRules(packet.getDstIP(), packet.getDstPort()) == 'Accept'


        else:
            print("packet comes to our server..")
            print("source ip:{} and port:{} will {}".format(packet.getSrcIP(),\
                                                                      packet.getSrcPort(),\
                                    r.checkInboundRules(packet.getSrcIP(), packet.getSrcPort())))
            print("Destination ip:{} and port:{} will {}".format(packet.getDstIP(),\
                                                                      packet.getDstPort(),\
                                    r.checkInboundRules(packet.getDstIP(), packet.getDstPort())))
            isSuccess = r.checkInboundRules(packet.getSrcIP(), packet.getSrcPort()) == 'Accept' and \
                        r.checkInboundRules(packet.getDstIP(), packet.getDstPort()) == 'Accept'



        if(isSuccess):
            print("Packet transmission successfull")
        else:
            print("Packet transmission unsuccessfull!!! Packet Dropped")

        print("\n\n")
            



        
    
'''
f = open('../packets/tcp.txt','r')
g = open('../packets/udp.txt','r')  
main(f)

'''
