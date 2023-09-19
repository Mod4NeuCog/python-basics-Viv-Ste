# NEURON 1

import sys

def main ():
    #setting the inital membrane potential
    membranep = float(-70)

    #getting the spike value from the terminal window
    spike = float(sys.argv[1])
    
    #we are adding a weight to the output depending on how large the spike value is
    if spike >= 25:
        weight = 3.0
    else:
        weight = 0.8 
    
    #updating membrane potential value
    membranep = membranep + spike
    
    if membranep >= -65 :
        #this is when we will output a spike of 5mv
        print (5* weight)
    else:
        #this is when we will output a spike of 0mv
        print (0)

if __name__ == '__main__':
    main ()


# NEURON 2

import sys

def main ():
    #setting the inital membrane potential
    membranep = float(-70)

    #getting the spike value from neuron1.py file
    inputspike = input()
    inputspike = float(inputspike)
    print ('neuron 2 recieved input spike', inputspike, 'mv')


    #updating membrane potential value
    membranep = membranep + inputspike
    
    if membranep >= -70 :
        #this is when we will output a spike of 5mv
        print ('The membrane potential has increased to', membranep, 'mv')
    else:
        #this is when we will output a spike of 0mv
        print ('The membrane potential has not changed')

if __name__ == '__main__':
    main ()

#changing the weight of the output modulates the change in the membrane potential of neuron two based on the intensity of the input to neuron 1.
