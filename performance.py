#!/usr/bin/python3

import ioTracer
from subprocess import *
import time
import signal

def runIOTest (isTracerOn):
    #start tracer
    if isTracerOn:
        process = Popen(['./driver.py'])

    t_start = time.perf_counter() # record start time
    retValue = call(['sh', './Tests/IOtest.sh'])

    t_end = time.perf_counter() # record end time

    #stop tracer
    if isTracerOn:
        process.send_signal(signal.SIGINT)
    return t_end - t_start



outputFile = open("performance.txt", 'w')
outputFile.write("Performance Output")
numTests = 50
count = 0
for i in range(numTests):
    a = runIOTest(False)
    outputFile.write("Total time elapsed without tracer: " + str(a) + '\n')
    count += a
outputFile.write("\nAverage time spent without tracer: " + str(count/numTests) + '\n')

count = 0
for i in range(50):
    a = runIOTest(True)
    outputFile.write("Total time elapsed with tracer: " + str(a) + '\n')
    count += a
outputFile.write("\nAverage time spent with tracer: " + str(count/numTests) + '\n')

outputFile.close()
