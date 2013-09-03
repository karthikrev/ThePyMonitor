import multiprocessing
from utils import Oscillator
from scheduler import Scheduler
from dispatcher import Dispatcher


def main():
    tasksq = multiprocessing.Queue()
    mgr = multiprocessing.Manager()
    e = mgr.Event()


    scheduler = Scheduler(e, tasksq)               # Reads the probs to be executed and queues in tasksq
    dispatcher = Dispatcher(tasksq)
    o = Oscillator(e, 1)                                    # TODO: this should be a configuration
    o.start()
    scheduler.start()
    dispatcher.start()
    o.join()
    scheduler.join()


if __name__ == '__main__':
    main()
