import multiprocessing
import logging
from managers import Connmgr, Datamgr

class Scheduler(multiprocessing.Process):           # TODO: Keyboardinterrupt handle it
    def __init__(self, event, queue):
        self.event = event
        self.dataprovider = Datamgr()
        self.queue = queue
        super(Scheduler, self).__init__()

    def run(self):
        try:
            while True:
                self.event.wait()
                for task in self.dataprovider.probs_to_run_now():
                    self.queue.put(task)
        except KeyboardInterrupt:
            pass


class Dispatcher(multiprocessing.Process):      # TODO: Keyboardinterrupt handle it
    def __init__(self, queue):
        self.queue = queue
        self.connection = Connmgr()
        super(Dispatcher, self).__init__()

    def run(self):
        while True:
            next_task = self.queue.get()
            if next_task is None:
                break
            else:
                print next_task
                self.connection.call()      # Get hostname and port of client to connect to from sqlite

