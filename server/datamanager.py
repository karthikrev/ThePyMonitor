
###############
# Managers
##############

import sqlite3
import datetime

class Datamanager:
    def __init__(self):
        self.dbfile = "/Users/knamasi/workspace/ThePyMonitor/data/monitor.db"      # TODO: Change this
        self.con = sqlite3.connect(self.dbfile)

    def probs_to_run_now(self):
        query = """select host.name, probe.name, probe.interval from
                    hostprobe, host, probe where host.id=hostprobe.host_id and probe.id=hostprobe.probe_id
                    and (strftime('%s', 'now')) % probe.interval = 0;"""
        for r in self.con.execute(query):      #Iterator of Array of tuples
            yield r
