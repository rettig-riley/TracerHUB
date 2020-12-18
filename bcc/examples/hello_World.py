#!/usr/bin/python3

from bcc import BPF

program = """
	int hello(void *ctx) {
		bpf_trace_printk ("Hello World\\n!");
		return 0;
	}
"""

b =  BPF(text = program)
b.attach_kprobe(event = "sys_clone", fn_name = "hello")
b.trace_print()
