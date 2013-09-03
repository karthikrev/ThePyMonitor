import multiprocessing
import logging
from connmanager import Connmanager

class Dispatcher(multiprocessing.Process):      # TODO: Keyboardinterrupt handle it
    def __init__(self, queue):                  # Args: Queue
        self.queue = queue                      # Queue IPC
        self.connection = Connmanager()             # Connecting to remote system using protocol xmlrpc | http | zmq | ...
        super(Dispatcher, self).__init__()

    def run(self):
        while True:
            next_task = self.queue.get()        # If queue has a task
            if next_task is None:
                break
            else:
                print next_task
                self.connection.connect()          # Connect to the remote using above mentioned protocol 
