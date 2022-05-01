import socket
from pysnmp.hlapi import *

class SNMPv2SecManager(object):

    def __init__(self):
        self.engine = SnmpEngine()
        self.hostname = input("IP address?")
        self.target = '192.168.1.14'
        self.port = 162

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serversocket.bind((self.hostname, self.port))


manager = SNMPv2SecManager()
while True:
    command = input("request: ")
    #g = getCmd(manager.engine,CommunityData('public'),)




