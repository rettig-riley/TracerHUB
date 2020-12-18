#!/usr/bin/python3

from bcc import BPF

# This may not work for 4.17 on x64, you need replace kprobe__sys_clone with kprobe____x64_sys_clone
#BPF(text='int kprobe__sys_clone(void *ctx) { bpf_trace_printk("Hello, World!\\n"); return 0; }').trace_print()

program = """
int hello(void *ctx) {
	bpf_trace_printk ("Hello World\\n!");
	return 0;
}
"""

b =  BPF(text = program)

# Attach a kprobe (kernel probe) to "listen" for clone syscalls, then run C code
b.attach_kprobe(event = b.get_syscall_fnname("clone"), fn_name = "hello")

# Allows for a more graceful exit upon keyboard interrupt
try:
    b.trace_print()
except KeyboardInterrupt:
    exit()
