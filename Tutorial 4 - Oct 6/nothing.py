#initial variables
Vrest = -70
spike = 0
Vmembrane = float(Vrest)

def main ():
    print ('What method of synaptic modelling do you want to use?')
    method_choice = int(input('Enter 1 to use method 1 and 2 to use method 2: '))
    simulate (method_choice)

def UpdateMemPotential1(Vmembane):
    spike = float(input('enter a spike value: '))
    Vmembrane = Vmembrane + spike
    return (Vmembrane)

def UpdateMemPotential2(Vmembane):
    spike = float(input('enter a spike value: '))
    Vmembrane = Vmembrane + spike
    return (Vmembrane)

def Simulate(method, Input):
    if method == 1:
        Vmembane = UpdateMemPotential1(Vmembane)
    elif method == 2:
        Vmembane = UpdateMemPotential2(Vmembane, Input)
    else:
        print ('ERROR')
    return Vmembrane

if __name__ == '__main__':
    main ()
    print(Vmembane)
