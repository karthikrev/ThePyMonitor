


class Connmanager:
    def __init__(self):
        pass

    def connect(self):
        print "Connecting"

#    def call(self):                                         # , address, port, ticket, probe, parameter):
#        url = "http://%s:%s/xmlrpc/" % (address, port)      # TODO: Should be variable from sqlite db file
#        proxy = xmlrpclib.ServerProxy(url, allow_none=True)
#        if parameter_string:
#            parameter = parameter_string.split(',')
#        else:
#            parameter = None
#        print ticket
#        res = proxy.cmd_submit_reading(ticket, probe, parameter)
#        return
