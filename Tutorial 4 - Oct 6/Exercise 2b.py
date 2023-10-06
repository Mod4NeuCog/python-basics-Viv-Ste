V_threshold = -65
V_membrane = -75
V_rest = -75
import time
#this is real time
start_time = time.time()
#this is simulation time
sim_time = 0


def delta(V_mem, i):
    n1_spikeList = [0, 1, 1, 0, 0, 0, 1]
    n2_spikeList = [1, 0, 1, 1, 1, 0, 1]
    n3_spikeList = [1, 0, 0, 1, 1, 1, 1]
    n4_spikeList = [0, 1, 0, 0, 1, 1, 0]
    n5_spikeList = [0, 1, 1, 0, 1, 0, 0]
    n6_spikeList = [1, 1, 1, 1, 1, 1, 1]
    n7_spikeList = [1, 0, 1, 0, 1, 0, 1]
    inputWeightList = [0.9, 1.5, 2.0, 0.5, 0.8, 1.2, 1.7]

    total_input = (n1_spikeList[i]*inputWeightList[i] + n2_spikeList[i]*inputWeightList[i] + n3_spikeList[i]*inputWeightList[i] + n4_spikeList[i]*inputWeightList[i] + n5_spikeList[i]*inputWeightList[i] + n6_spikeList[i]*inputWeightList[i] + n7_spikeList[i]*inputWeightList[i])
    
    V_mem = V_mem + total_input
    return(V_mem)

def lambda_dtss(V_mem):
    if(V_mem >= V_threshold):
        global V_membrane
        V_membrane = V_rest
        return(5)
    else:
        return(0)

## Define a function to simulate neuron behaviour
def simulate(t_end):
    sim_time=0
    global V_membrane
    while(sim_time < t_end):
        output_neuron = lambda_dtss(V_membrane)
        V_membrane = delta(V_membrane, sim_time)
        
        current_time_real = time.time() - start_time
        print('the real time elapsed is: ', current_time_real)
        print("V_membrane=",V_membrane)
        print("simulation time is: ", sim_time, V_membrane,output_neuron)

        sim_time = sim_time + 1
        current_time_sim = sim_time
        print('the simulation time elapsed is: ', float(current_time_sim))

        #print("n=",n,"t=", sim_time)
    return(V_membrane)    

def main():
    t_end = 7.0
    simulate(t_end)

if __name__ == '__main__':
  main()