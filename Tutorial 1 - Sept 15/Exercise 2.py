# mod_neur1 is a model neuron we are observing
# mod_neur2 is a presynaptic neuron for mod_neur1
#membranep is the membrane potential of the hypothetical mod_neur1 neuron

#this initializes the variable that allows the beginning of the program
start = 0
membranep = -10

def main (membranep):
    #the inital membrane potential
    membranep = -15 #this is an integer
    x = 0 #this is an integer
    #this describes this situation
    print('You are a presynaptic neuron, 1 means you have a propagated AP and 0 means you are resting.')

    #this code block is a loop and breaks the loop once the neuron has reached its critical threshold of -5 to fire and AP
    while membranep < -5:
        mod_neur0 =int(input('Enter your current state 1 or 0: '))
        x = x + 1
        if mod_neur0 == 0:
            continue
        else:
            membranep = membranep + 0.7*x #this variable is now a float variable because the integer was multiplied by a float
    return(membranep)

#this section causes the use of the main function
if start == 0:
    print('Neuron fires an membrane potential.', main(membranep))


#when membranep is initialized to 1.0, it is a float variable and remains one after being multiplied by 0.7