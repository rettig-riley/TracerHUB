#!/bin/sh
# Performance Testing script to simulate a IO-intensive workload

# stress-ng will add two io stressors and then run for 5000 operations
stress-ng --io 2 --cpu-ops 5000



