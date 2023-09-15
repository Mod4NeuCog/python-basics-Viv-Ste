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
    
    if membranep >= -65 :
        #this is when we will output a spike of 5mv
        print ('The membrane potential has increased to', membranep, 'mv')
    else:
        #this is when we will output a spike of 0mv
        print ('The membrane potential has not changed')

if __name__ == '__main__':
    main ()

#if n1_spike == 5:
#    n2_membranep = n2_membranep + n1_spike
#    print ('Membrane potential hase been changed to:' , n2_spike)
#else:
#    print ('No change to membrane potential.')
