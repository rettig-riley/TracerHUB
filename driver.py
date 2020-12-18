#!/usr/bin/python3
import os
import ioTracer

print ("Basic tracer HUB will update information for I/O operations, TCP system calls, and memory every 60 second")
print ("Special notifications will appear in a unique screen when limits are being reached")

# FIXME For now all information will be printed in a single terminal, I would like to crate different windows or widgets using tkinter for each though

ioTracer.traceIO(1)


# os.system('bcc/tools/biolatency.py') # Gives report on block device I/O

