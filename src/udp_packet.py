class udp_packet():

    def __init__(self, MACaddress, srcIP, dstIP, srcPort, dstPort):
        self.MACaddress = MACaddress
        self.srcIP = srcIP
        self.dstIP= dstIP
        self.srcPort = srcPort
        self.dstPort = dstPort

    def getMACaddress(self):
        return self.MACaddress

    def getSrcIP(self):
        return self.srcIP

    def getMACaddress(self):
        return self.MACaddress
    
    def getDstIP(self):
        return self.dstIP

    def getSrcPort(self):
        return self.srcPort

    def getDstPort(self):
        return self.dstPort

    def String(self):
        return "UDP packet: Src_ip:{0} Dst_ip:{1} Src_port:{2} Dst_port:{3}".format(self.srcIP,self.dstIP, self.srcPort,self.dstPort)
