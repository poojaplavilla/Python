#!/usr/bin/python2

import sys

def mode0():
	print("MODE 0")
def mode1():
	print("MODE 1")
def mode2():
	print("MODE 2")
def mode3():
	print("MODE 3")

def main():
	mode=sys.argv[1]                #Give input using CLA...
        if mode=='0':
                mode0()
        elif mode=='1':
                mode1()
        elif mode=='2':
                mode2()
        elif mode=='3':
                mode3()
        else:
             	print("Invalid it is...!!!")

if __name__=='__main__':
        main()

