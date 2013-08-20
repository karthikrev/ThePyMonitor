import os
import sqlite3

class SqliteReader:
    def __init__(self):
        self.dbfile = "monitor.db"
        self.con = sqlite3.connect(self.dbfile)
    
    def to_run_now(self):
        query = """select host.name, probe.name, probe.interval from 
                    hostprobe, host, probe where host.id=hostprobe.host_id and probe.id=hostprobe.probe_id 
                    and (strftime('%s', 'now')) % probe.interval = 0;"""
        for r in self.con.execute(query):      #Array of tuples
            yield r 

s = SqliteReader()
for run_now in s.to_run_now():
    print run_now
