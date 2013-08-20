
###############
# Managers
##############

import sqlite3
import datetime

class Sqlitemgr:
    def __init__(self):
        self.dbfile = "/Users/knamasivayam/workspace/ThePyMonitor/data/monitor.db"      # TODO: Change this
        self.con = sqlite3.connect(self.dbfile)

    def to_run_now(self):
        query = """select host.name, probe.name, probe.interval from
                    hostprobe, host, probe where host.id=hostprobe.host_id and probe.id=hostprobe.probe_id
                    and (strftime('%s', 'now')) % probe.interval = 0;"""
        for r in self.con.execute(query):      #Iterator of Array of tuples
            yield r


class Datamgr:
    def __init__(self):
        self.dataprovider = Sqlitemgr()

    def probs_to_run_now(self):
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for run_now in self.dataprovider.to_run_now():
            yield run_now

class Connmgr:
    def __init__(self):
        pass

    def call(self, address, port, ticket, probe, parameter):
        url = "http://%s:%s/xmlrpc/" % (address, port)      #TODO: Should be variable from sqlite db file
        proxy = xmlrpclib.ServerProxy(url, allow_none=True)
        if parameter_string:
            parameter = parameter_string.split(',')
        else:
            parameter = None
        print ticket
        res = proxy.cmd_submit_reading(ticket, probe, parameter)
        return

