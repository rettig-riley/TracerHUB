#!/usr/bin/python
# Counts number of io operations and reports at every set interval
# Based off of disksnoop.py, but simplified

from bcc import BPF
from time import sleep
from datetime import datetime


def traceIO(time):
    # Number of seconds between each report
    reportTime = time

    program = """

    // Create hash table with key of and value both of type u64 (default)
    BPF_HASH(ioops);


    int countio(struct pt_regs *ctx) {

        u64 key = 1; // I believe this can be arbitrary, as we only need one key
        u64 counter = 0; // Start count of io operations at 0
        u64 *p; 

        p = ioops.lookup(&key); // bcc's version of BPF lookup 
        
        // Have to check whether a pointer is null before dereferencing, or else it will not compile (restricted C)
        if (p != 0){ 
            counter = *p;
        }

        // Increase counter because this function will only ever be called when an io operation is completed
        counter++;
        
        // Update hash table at key with counter
        ioops.update(&key, &counter);

        return 0;
    }
    """

    b =  BPF(text = program)

    # Attach a kprobe (kernel probe) to "listen" for completed io operations, then run C code
    b.attach_kprobe(event="blk_account_io_done", fn_name="countio")

    print('Reporting total number or I/O operations completed every ' + str(reportTime) + ' second(s)')
    # header
    print("%-12s %-2s" % ("TIME", "# of IO operations completed"))

    # Only report on new 
    lastTotalIO = 0;
    while True:
        try:
            sleep(reportTime) # Wait reportTime sec between each report
            
            # We only expect one
            #print(b["ioops"].items())
            for k,v in b["ioops"].items():
                curr = v.value - lastTotalIO
                #print((datetime.now().strftime("%H:%M:%S"), curr))
                print("%-12s %-2s %-10s" % (datetime.now().strftime("%H:%M:%S"), curr, "*" * curr))
                lastTotalIO = v.value
        
        # More graceful exit
        except KeyboardInterrupt:
            print("Total Number of IO operations reported were: " + str(lastTotalIO))
            exit()
