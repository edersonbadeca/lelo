# coding: utf-8
# Author: João S. O. Bueno

from multiprocessing import Process, Queue


a = Process()

def _xecuter(queue, func, args, kwargs):
    queue.put(func(*args, **kwargs))


#q = Queue(1)
#a = Process(target = soma, args=(q, 2, 3) )

#x = a.start()
#print q.get()



def paralell(func):
    """
    Make so that the function is called in a separate process, 
    using Python multiprocessing, and gets started imediatelly -
    in a non blocking way.
    The return value is a proxy object that will bridge to the real
    return value whenever it is used - it will block at time
    of use if it is not complete
    """
    pass
