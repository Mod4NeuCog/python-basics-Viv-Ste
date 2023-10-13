class Neuron:
    def __init__(self, cell_type, axon):
        self.cell_type = cell_type
        self.axon = axon
        self.membranePotential = -75

    def update_mem_potential (self, input_spikes):
        self.membranePotential = self.membranePotential + input_spikes
        return (self.membranePotential)

    def output (self):
        if (self.membranePotential >= -60):
            self.membranePotential = -75
            return (5)
        else:
            return (0)
    
    #here you can add a static stock thing
    #CLASSES DONOT = OBJECTS

# from name_of_directory.name_of_class_file import name_of_the_class
# from Pyramidal_Neur import Pyramidal_Neur
# from Ovoid_Neur import Ovoid_Neur


# def main ():
#     neuron1 = Neuron("glia", 5)
#     pyramid1 = Pyramidal_Neur(5000, 50, 'DA')
#     ovoid1 = Ovoid_Neur(10)
#     return (neuron1, pyramid1, ovoid1)

# if __name__ == '__main__':
#     print (main())

