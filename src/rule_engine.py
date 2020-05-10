import configparser

class rule_engine():
    def __init__(self):
        self.in_config = configparser.ConfigParser()
        self.out_config = configparser.ConfigParser()
        self.in_config.read('src/inbound rules.ini')
        self.out_config.read('src/outbound rules.ini')

    def checkInboundRules(self, ip_address, port):

        for i in self.in_config['Accepting ip']:
            if(i == ip_address and port in self.in_config['Accepting ip'][i].split(",")):
                return "Accept"

        for i in self.in_config['Declining ip']:
            if(i == ip_address and port in self.in_config['Declining ip'][i].split(",")):
                return "Decline"


        for i in self.in_config['Rejecting ip']:
            if(i == ip_address and port in self.in_config['Rejecting ip'][i].split(",")):
                return "Reject"

        return "No rule associated!!!! Please assign a rule"



    
    def checkOutboundRules(self, ip_address, port):
        for i in self.out_config['Accepting ip']:
            if(i == ip_address and (port in self.out_config['Accepting ip'][i].split(","))):
                return "Accept"

        for i in self.out_config['Declining ip']:
            if(i == ip_address and (port in self.out_config['Declining ip'][i].split(","))):
                return "Decline"


        for i in self.out_config['Rejecting ip']:
            if(i == ip_address and (port in self.out_config['Rejecting ip'][i].split(","))):
                return "Reject"

        return "No rule associated!!!! Please assign a rule"
    


'''
r = rule_engine()
print(r.checkOutboundRules('192.168.1.6','63449'))
print(r.checkInboundRules('54.192.151.48','443'))
'''
'''
print(r.checkOutboundRules('192.168.1.6','63439'))  # should return Reject
print(r.checkOutboundRules('192.168.1.6','55173'))  # should return Accept
print(r.checkOutboundRules('192.168.1.6','57762'))  # should return Decline
print(r.checkOutboundRules('192.168.2.6','57762'))  # should return No rule associated !!! (No Ip)
print(r.checkOutboundRules('192.168.2.6','1'))      # should return No rule associated !!! (No Port)



print(r.checkInboundRules('192.168.1.4','2054'))  # should return Reject
print(r.checkInboundRules('142.250.4.93','443'))  # should return Accept
print(r.checkInboundRules('198.252.206.25','443'))  # should return Decline
print(r.checkInboundRules('192.168.2.0','443'))  # should return No rule associated !!! (No Ip)
print(r.checkInboundRules('192.168.1.4','1')) # should return No rule associated !!! (No Ip)
'''
