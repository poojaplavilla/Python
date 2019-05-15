#!/usr/bin/python2

#function with no arguments...
print("Hello1")
def Hello():
	print("Hello6")
print("Hello2")
#main function...

def main():
	print("Hello5")
        Hello()                     #Calling Hello() method...
print("Hello3")

if __name__=='__main__':
        print("Hello4")
        main()
	print("Hello7")

#First '__main__' will get executed...
