#!/usr/bin/python3
import os, time
i = 0
def cpu_frequency():
	while i != 1:
		os.system('clear')
		os.system('grep MHz /proc/cpuinfo')
		time.sleep(1)
		os.system('clear')
cpu_frequency()
