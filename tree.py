#!/usr/bin/python3

import sys

z = input("how tall do you want the tree? :\n")
if(z == "forest"):
	s = 7
else: 
	s = (int(z))+1
i = s-1
d = i-2
print("")
if(z == "forest"):
	for x in range(0, s):
		a = i
		i = i - 1
	while(a > 0):
		sys.stdout.write(" ")
		a = a-1		
	for y in range(0, 2*x -1):
		sys.stdout.write("*")
	print("")
	for r in range(0, 2):
		for g in range(0, d):
			sys.stdout.write(" ")
		print("***")	
for x in range(0, s):
	a = i
	i = i - 1
	while(a > 0):
		sys.stdout.write(" ")
		a = a-1		
	for y in range(0, 2*x -1):
		sys.stdout.write("*")
	print("")
for r in range(0, 2):
	for g in range(0, d):
		sys.stdout.write(" ")
	print("***")	
