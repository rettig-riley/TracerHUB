# TracerHUB
Final Project for CS341

## Setup
The bcc file is included with this repo, although there are some other tool dependecies. I installed from the source following the directions in [INSTALL.md](https://github.com/iovisor/bcc/blob/master/INSTALL.md#ubuntu---source) on the bcc github page.

## IO Tracing
I have based this roughly off of the biolatency.py tool, but more simplistic. I am simply attaching a kprobe to a blk_account_io_done event (I've decided this event rather than blk_account_io_complete event, which may be called multiple times, per [this](https://github.com/iovisor/bcc/issues/2091) conversation). I use bcc's map to keep track of the count of these events. 

## Driver Notes
