# mod_neur1 is a model neuron we are observing
# mod_neur2 is a presynaptic neuron for mod_neur1
#membranep is the membrane potential of the hypothetical mod_neur1 neuron

#this initializes the variable that allows the beginning of the program
start = int(0)
membranep = int(-10)

def main (membranep):
    #the inital membrane potential
    membranep = int(-15) #this is an integer
    x = int(0) #this is an integer
    #this describes this situation
    print('You are a presynaptic neuron, 1 means you have a propagated AP and 0 means you are resting.')

    #this code block is a loop and breaks the loop once the neuron has reached its critical threshold of -5 to fire and AP
    while membranep < -5:
        mod_neur0 =int(input('Enter your current state 1 or 0: '))
        x = x + 1
        if mod_neur0 == 0:
            continue
        else:
            membranep = membranep + 1*x
    return(membranep)

#this section causes the use of the main function
if start == 0:
    print('Neuron fires an membrane potential.', main(membranep))