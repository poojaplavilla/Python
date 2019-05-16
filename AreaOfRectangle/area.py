#Program to calculate area of rectangle...
#Input is given	using CLA...
#Area is calulcated if only integer values are passed...
#Display msg if	invaid inputs given by user...

#!/usr/bin/python2

import sys

def main():
	a=sys.argv              #Give input using CLA...

        if(len(a) == 1):
                print("Invalid number of arguments")

        elif(a[1].isdigit() and a[2].isdigit()):
                print("Length of rectangle: " + a[1])
                print("Breadth of rectangle: " + a[2])
                area=(int(a[1])*int(a[2]));
                print("Area of rectangle: " + str(area))

        else:
             	print("Invalid arguments...!!!")

if __name__=='__main__':
        main()
