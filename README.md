# TracerHUB
Final Project for CS341

## Setup
The bcc file is included with this repo, although there are some other tool dependecies to run. I installed these following the directions in [INSTALL.md](https://github.com/iovisor/bcc/blob/master/INSTALL.md#ubuntu---source) on the bcc github page, which will explain how to install based on your system.\

For my tests I also used `stress-ng`, which can be installed with `sudo apt install stress-ng`\

Note: TracerHUB is built and tested in a virtual machine running Ubuntu 18.04

# Files/directories
The ProjectGutenberg directory is a collection of a few text files used for testing\
`hello.py` is a simple script that prints "Hello World" at every `clone` syscall that is traced\
`ioTracer.py` tracks IO operations (more below)\
`performance.py` is the driver for testing overhead of scripts (more below)

## IO Tracing
I have based this roughly off of the `biolatency.py` tool, but more simplistic. I am simply attaching a kprobe to a blk_account_io_done event (I've decided this event rather than blk_account_io_complete event, which may be called multiple times, per [this](https://github.com/iovisor/bcc/issues/2091) conversation). I use bcc's map to keep track of the count of these events and return this to the user space.

## TCP System Call Tracing
TO-DO\
Tracks counts of TCP-relevent system calls including `socket()`, `bind()`, `listen()`, `accept()`, `send()`, and `receive()`\
![TCP System Call Diagram From IMB](https://developer.ibm.com/developer/default/articles/au-tcpsystemcalls/images/Layers.gif)

## Performance Testing
The testing suite for TracerHUB uses `stress-ng` which can stress test a computer system in a controlled way, allowing you to pick which components are stressed. See [here](https://manpages.ubuntu.com/manpages/artful/man1/stress-ng.1.html) for documentation. I have set up a few shell scripts running these `stress-ng` commands, which can be found in the Tests directory. All tests can be run by running `performance.py`. Output will be written to `performance.txt` which will demonstate overhead of bcc scripts.

## Bugs and To-Do
Still need to finish implementing TCP and driver