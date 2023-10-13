from Neuron import Neuron

class Pyramidal_Neur(Neuron):
    def __init__(self, dendrites, axon, neurotransmitter):
        super().__init__("Pyramidal Neuron", dendrites, axon, neurotransmitter)
        self.neurotransmitter = neurotransmitter


