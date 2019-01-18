"""This module contains class of network."""
class NeuralNetwork:
    """
    This is class which stores all information about the network
    and has its state.
    """
    _number_of_layers = None
    _layer_sizes = None
    _neurons = None
    _connections = None
    def __init__(self):
        pass
    def clear_totally(self):
        """ This method erares all data of network."""
    def set_number_of_layers(self, number):
        """This method sets number of layers in network."""
        if ~isinstance(number, int):
            return
        if number < 1:
            return
        self._neurons = None
        self._connections = None
        self._number_of_layers = number
        self._layer_sizes = [0] * number
        self._neurons = [None] * number
        self._connections = [None] * (number - 1)
        # Connections are numbered is way that 0 means after 0 layer.
    def set_layer_size(self, which_layer, size):
        """This method sets quantity of neurons in indexed layer.

Layer 0 is input. Layer number - 1 is the output.
        """
        if ~isinstance(which_layer, int) or ~isinstance(size, int):
            return
        if which_layer < 0 or which_layer >= self._number_of_layers:
            return
        if size < 1:
            return
        self._layer_sizes[which_layer] = size
        self._neurons[which_layer] = [0.0] * size
    def init_with_zeros(self):
        """This function shall create the neurons and their connections
and everything that is necessary this network to work.
        """
        if self._number_of_layers is None:
            return
        for i in self._layer_sizes:
            if ~isinstance(i, int) or i < 1:
                return
        for i in self._neurons:
            for j in range(self._layer_sizes[i]):
                self._neurons[j] = 0.0
        for i in range(self._number_of_layers - 1):
            self._connections[i] = [0.0] \
             * ((self._layer_sizes[i] + 1) * self._layer_sizes[i+1])
            # + 1 because of bias

    def set_func(self, where, func):
        """This function is to set the function between layer 'layer' and next.

This is not finished. Here I need to add derivatires somehow and I
don't know how. It is temporary.
        """
    def randomize_weights(self):
        """This function randomizes all weights in all connections and biases.
        """
    def fill_input(self, numbers):
        """This function fills input.

I do not know how yet. xD
        """
    def get_input(self):
        """Returns some table of input numbers"""
    def set_input_number(self, where, number):
        """Set one number in input."""
    def get_input_number(self, where, number):
        """ygrdfgtr"""
    def calculate(self):
        """Calculate output from network with actual input."""
    def propagate_back(self, wanted_output):
        """This function makes network to learn using calculated output and
wanted output.
        """
    

