###########################################################################
from enum import Enum

class HostType(Enum):
   '''
        Types of hosts
   '''
   CLIENT = 0
   SERVER = 1

class PacketSwitchType(Enum):
   '''
        Types of packet switches
   '''
   ROUTER = 0
   LINKLAYER = 1

class ProtocolType(Enum):
   '''
        Types of packet switches
   '''
   FTP = 0
   IP = 1

###########################################################################
class Network():
    '''
        The network and its architecture
    '''
    def __init__(self,hosts = [],isps = []):
        self.hosts = hosts
        self.isps = isps

    def connect(self):
        raise Exception()

class Host():
    '''
        The end systems
    '''
    def __init__(self,type = HostType.CLIENT):
        self.type = type

class ISP():
    '''
        The internet service provider
    '''
    def __init__(self,name):
        self.name = name

class PacketSwitch():
    '''
        The packet switch helps in receiving and forwarding data packets
    '''
    def __init__(self,type = PacketSwitchType.ROUTER):
        self.type = type

class Packet():
    '''
        The actual information being transferred
    '''
    def __init__(self):
        self.info = "Some Message"

class Protocol():
    '''
        A way to communicate between devices
    '''
    def __init__(self,type = ProtocolType.FTP):
        self.type = type
    
###########################################################################

hostA = Host() 
hostB = Host()
hostList = [hostA,hostB]
ispA = ISP("SAFARICOM")
ispList = [ispA]

Internet = Network(hosts = hostList,isps = ispList)
print(Internet.hosts,Internet.isps)