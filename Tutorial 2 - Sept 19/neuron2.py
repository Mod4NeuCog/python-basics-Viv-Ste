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
