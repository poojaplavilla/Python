#!/usr/bin/python2

def Hello(fname,lname):                 #function with 2 parameters...
        var = fname + ' ' +  lname
        return var                      #returing 1 value...

def main():
	fname='Pooja'                         #storing a value in a variable...
        lname='Plavilla'                #storinf 2nd value in a variable
        text= Hello(fname,lname)        #storing a function in a variable...
        print('Full name is: ' + text)  #printing that function...

if __name__=='__main__':
        main()

