import logging
from datetime import datetime

from pysnmp import debug
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context, ntforg
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder


# pysnmp debugging on
debug.setLogger(debug.Debug('all'))

formatting = '[%(asctime)s-%(levelname)s]-(%(module)s) %(message)s'
logging.basicConfig(level=logging.DEBUG, format=formatting, )

logging.info("Starting....")


class SNMPv2SecAgent(object):
    """ Implementa um agente que vai servir uma MIB customizada

        Neste agent proxy vou ter apenas referência das MIBs a que têm acesso

        Não vou saber valores dos objectos pedidos
    """
    def __init__(self):

        # Create SNMP engine
        self.snmpEngine = engine.SnmpEngine()

        # open a UDP socket on port 161 to listen for snmp requests
        config.addSocketTransport(self.snmpEngine, udp.domainName,udp.UdpSocketTransport().openServerMode(('',161)))

        # Here we configure two distinct Community Strings to control read and write
        # operations. public --> Read only, private --> Read/Write
        config.addV1System(self.snmpEngine, "agent", "public")
        config.addV1System(self.snmpEngine, 'my-write-area', 'private')


    def encrypt(self,data):
        pass

    def decrypt(self,data):
        pass












