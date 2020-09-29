#!/usr/bin/python3
import os, time
def cpu_frequency_linux():
	while True:
		os.system('clear')
		os.system('grep MHz /proc/cpuinfo')
		time.sleep(1)
		os.system('clear')

def cpu_information_windows():
	while True:
		os.system("cls")
		os.system("wmic cpu list brief")
		time.sleep(1)
def cpu_information_linux():
	while True:
		os.system("clear")
		os.system("lscpu")
		time.sleep(1)
systemtype = input('What system to you use? [1] Windows [2] Linux. : )
if systemtype == 1:
	cpu_information_windows()
elif systemtype == 2:
	chinf = input("What information you want to collect? [1] Infomation about CPU [2] CPU frequency : ")
		   
