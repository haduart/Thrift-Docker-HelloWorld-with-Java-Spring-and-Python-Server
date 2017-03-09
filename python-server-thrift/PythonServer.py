#!/usr/bin/env python

import sys
import os


sys.path.append('gen-py')

from ReportingService import ReportService
from ReportingService.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

reload(sys)
sys.setdefaultencoding('utf-8')


class ReportServiceHandler:
    def __init__(self):
        self.log = {}

    def createReport(self, reportName, events, reportType, userName):
        print('createReport reportName %s' % reportName)
        print('createReport reportType %s' % reportType)
        print('createReport userName %s' % userName)

        try:
            return "createReport executed"
        except:
            print sys.exc_info()
            x = InvalidOperation()
            x.whatOp = 1
            x.why = 'There is an error'
            raise x


def start_server():
    handler = ReportServiceHandler()
    processor = ReportService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')

if __name__ == "__main__":
    start_server()
