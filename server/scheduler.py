import multiprocessing
import logging
from datamanager import Datamanager

class Scheduler(multiprocessing.Process):           
    def __init__(self, event, queue):               # Args: 1. Event object and  2. Queue
        self.event = event                          # Event object with which Scheduler is poked by oscillator every min
        self.dataprovider = Datamanager()               # The interface to configurations through sqlite/mysql/python script/xml/json/nagios model
        self.queue = queue                          # The Queue
        super(Scheduler, self).__init__()           

    def run(self):
        try:
            while True:
                self.event.wait()                   # Wait till oscillator pokes me
                for task in self.dataprovider.probs_to_run_now():	# Read the configs and check what to do now
                    self.queue.put(task)            # If anything is to be monitored now, add to Queue
        except KeyboardInterrupt:
            pass
