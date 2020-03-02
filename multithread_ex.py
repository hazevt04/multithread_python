#!/usr/bin/env python3

import os
import math
from random import random
from multiprocessing import Process, Queue

def generateData(num_items, data_queue):
    pname = "generateData"
    timeout_secs = 2
    blocking = True
    for i in range(num_items):
        t_data = random()
        print("{}: Generated data {}: {}".format(pname, i, t_data))
        data_queue.put(t_data, blocking, timeout_secs)
        print("{}: Data {} put into queue".format(pname, i))


def processData(num_items, data_queue):
    pname = "processData"
    for i in range(num_items):
        timeout_secs = 2
        blocking = True
        print("{}: Trying to get Data {} from queue".format(pname, i))
        t_data = data_queue.get(blocking, timeout_secs)
        
        print("{}: Got data {}: {}".format(pname, i, t_data))
        t_data_out = math.sqrt(t_data)
        print("{}: Result {} added to data_out".format(pname, i))
    


if __name__ == '__main__':
    num_items = 5
    data_queue = Queue()
    gen_proc = Process(target = generateData, args = (num_items,data_queue,))
    proc_proc = Process(target = processData, args = (num_items,data_queue,))
    
    gen_proc.start()
    proc_proc.start()
    
    gen_proc.join()
    proc_proc.join()
    
    print("Done with both procs. Exiting")
