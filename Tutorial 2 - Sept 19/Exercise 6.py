def main ():
    print ('What method of synaptic modelling do you want to use?')
    print ('Method 1: modelling impact of synaptic weights on membrane potential.')
    print ('Method 2: modelling multiple inputs in time')
    method_choice = int(input('Enter 1 to use method 1 and 2 to use method 2: '))
    simulate (method_choice)

def simulate(method_choice):
    if method_choice == 1:
        membranep = float(-70)
        spike = float(input('Input a Spike value'))
        if spike >= 25:
            weight = 3.0
        elif 0<spike<25:
            weight = 1.8
        else:
            weight = 0
    
        membranep = membranep + spike

        if membranep >= -65 :
            #this is when we will output a spike of 5mv
            print ('output from neuron1 is:', 5* weight)
            print (membranep)
        else:
            #this is when we will output a spike of 0mv
            print (0)
    
    elif method_choice == 2:
        membranep = float(-70)
        x = int(0) 
        #this describes this situation
        print('You are a presynaptic neuron, 1 means you have a propagated AP and 0 means you are resting.')

        #this code block is a loop and breaks the loop once the neuron has reached its critical threshold of -50 to fire and AP
        while membranep < -50:
            model_neur0 =int(input('Enter your current state 1 or 0: '))
            x = x + 1
            if model_neur0 == 0:
                continue
            else:
                membranep = membranep + 1*x
                print("membrane potential is now:", membranep)    
    else:
        print ('error')


if __name__ == '__main__':
    main ()


