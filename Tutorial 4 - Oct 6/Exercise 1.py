V_threshold = -65
V_membrane = -75
V_rest = -75
import time
#this is real time
start_time = time.time()

#this is simulation time
sim_time = 0


def delta(input, V_mem):
    V_mem = V_mem + input
    return(V_mem)

def lambda_dtss(V_mem):
    if(V_mem >= V_threshold):
        global V_membrane
        V_membrane = V_rest
        return(5)
    else:
        return(0)

## Define a function to simulate neuron behaviour
def simulate(inputSpikeList,t_end,c):
    sim_time=0
    n=0
    global V_membrane
    while(sim_time < t_end):
        output_neuron = lambda_dtss(V_membrane)
        V_membrane = delta(inputSpikeList[n],V_membrane)
        #print("V_membrane=",V_membrane)
        #print("t=",t,V_membrane,output_neuron)
        current_time_real = time.time() - start_time
        print('the real time elapsed is: ', current_time_real)
        
        n=n+1
        sim_time=n*c

        current_time_sim = sim_time
        print('the simulation time elapsed is: ', current_time_sim)

        #print("n=",n,"t=",t)
    return(V_membrane)    

def main():
    inputSpikeList = [0,5,5,0,0,0,0,5]
    t_end = 3.5
    c = 0.5
    simulate(inputSpikeList,t_end,c)

if __name__ == '__main__':
  main()