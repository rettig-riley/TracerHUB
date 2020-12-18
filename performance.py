#!/usr/bin/python3

import ioTracer
import subprocess
import time


def runIOTest (isTracerOn):
    time.sleep(2)
    t_start = time.perf_counter() #record start time
    if isTracerOn:
        # Fix this later
        exit()
    retValue = subprocess.call(['sh', './IOtest.sh'])
    t_end = time.perf_counter()
    return t_end - t_start



print("Total time elapsed: " + str(runIOTest(False)))

