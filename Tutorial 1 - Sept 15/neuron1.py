import sys

def main ():
    #setting the inital membrane potential
    membranep = float(-70)

    #getting the spike value from the terminal window
    spike = float(sys.argv[1])

    #updating membrane potential value
    membranep = membranep + spike
    
    if membranep >= -65 :
        #this is when we will output a spike of 5mv
        print (5)
    else:
        #this is when we will output a spike of 0mv
        print (0)

if __name__ == '__main__':
    main ()
