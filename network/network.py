"""This module contains class of network."""

from random import uniform
from enum import IntEnum

from network import connections


class NeuralNetwork:
    """
    This is class which stores all information about the network
    and has its state.
    """
    _number_of_layers = None
    _layer_sizes = None
    _layer_functions = None
    _layer_derivaties = None # hmm... it is only sugestion now
    _neurons = None
    _connections = None

    def __init__(self):
        pass

    def _check_network_readiness(self):
        if ~isinstance(self._number_of_layers, int)
                or self._number_of_layers < 1:
            return False # no number of layers
        if ~isinstance(self._layer_sizes, list)
                or len(self._layer_sizes) != self._number_of_layers:
            return False # layer sizes not set good, very bad
        for i in self._layer_sizes:
            if ~isinstance(i, int) or i < 1:
                return False # layer sizes not set good, but not so bad
        if ~isinstance(self._neurons, list)
                or len(self._neurons) != self._number_of_layers:
            return False # there is an error with layer sizes
        for i, layer in enumerate(self._neurons):
            if ~isinstance()
        

    def clear_totally(self):
        """ This method erares all data of network."""
        self._number_of_layers = None
        self._layer_sizes = None
        self._layer_functions = None
        self._neurons = None
        self._connections = None

    def set_number_of_layers(self, number):
        """This method sets number of layers in network."""
        if ~isinstance(number, int) or number < 1:
            raise ValueError("set_number_of_layers: expected positive int")
        self._neurons = None
        self._connections = None
        self._number_of_layers = number
        self._layer_sizes = [0] * number
        self._layer_functions = [None] * (number - 1)
        self._neurons = [None] * number
        self._connections = [None] * (number - 1)
        # Connections are numbered is way that 0 means after 0 layer.


    def set_layer_size(self, which_layer, size):
        """This method sets quantity of neurons in indexed layer.

Layer 0 is input. Layer number - 1 is the output.
        """
        if ~isinstance(which_layer, int):
            raise ValueError("set_layer_size: expected 'which_layer' "
                             + "as an int")
        if ~isinstance(size, int):
            raise ValueError("set_layer_size: expected 'size' as an int")
        if ~isinstance(self._number_of_layers, int):
            raise ValueError("set_layer_size: number of layers is not set")
        if which_layer < 0 or which_layer >= self._number_of_layers:
            raise ValueError("set_layer_size: 'which_layer' has to be in [0,"
                             + self._number_of_layers
                             + ")")
        if size < 1:
            raise ValueError("set_layer_size: expected 'which_layer' as an "
                             + "positive int")
        self._layer_sizes[which_layer] = size
        self._neurons[which_layer] = [0.0] * size

    def init_with_zeros(self):
        """This function shall create the neurons and their connections
and everything that is necessary this network to work.
        """
        if self._number_of_layers is None:
            raise ValueError("init_with_zeros: number of layer not set")
        for i, layer_size in self._layer_sizes:
            if ~isinstance(layer_size, int) or layer_size < 1:
                raise ValueError("init_with_zeros: layer "
                                 + i
                                 + "is not a positive int")
        for i in self._neurons:
            for j in range(self._layer_sizes[i]):
                self._neurons[j] = 0.0
        for i in range(self._number_of_layers - 1):
            self._connections[i] = [0.0] \
             * ((self._layer_sizes[i] + 1) * self._layer_sizes[i+1])
            # + 1 because of bias

    def set_func(self, layer, func):
        """This function is to set the function between layer 'layer' and next.

This is not finished. Here I need to add derivatires somehow and I
don't know how. It is temporary.

Layer means destination layer index + 1

If function is not set this layer will be treated as linear (f(x)=x).
        """
        if ~isinstance(layer, int):
            raise ValueError("set_func: expected 'layer' as an int")
        if ~callable(func):
            raise ValueError("set_func: expected 'func' as a function")
        if ~isinstance(self._number_of_layers, int):
            raise ValueError("set_func: number of layers is not set")
        if layer < 0 or layer >= self._number_of_layers - 1:
            raise ValueError("set_func: expected 'layer' in [0,"
                             + (self._number_of_layers - 1)
                             + ")")
        self._layer_functions[layer] = func

    def randomize_weights(self, min_value, max_value):
        """This function randomizes all weights in all connections and biases.
        """
        if ~isinstance(min_value, (float, int)) \
                or ~isinstance(max_value, (float, int)):
            raise ValueError("randomize_wights: expected 'min_value' and "
                             + "'max_value' as floats or ints")
        if min_value > max_value:
            raise ValueError("randomize_wights: expected "
                             + "min_value <= max_value")
        if 
        for i in range(self._number_of_layers - 1):
            for j in range(len(self._connections[i])):
                self._connections[i][j] = uniform(min_value, max_value)

    def layer_get_one(self, layer, where):
        """oldsfklodsk"""
        return self._neurons[layer][where]

    def layer_set_one(self, layer, where, number):
        """lkdsflkadsl"""
        self._neurons[layer, where] = number

    def layer_get_all(self, layer):
        """ get whole layer xD """
        return self._neurons[layer].copy()

    def layer_set_all(self, layer, numbers):
        """ ustawia warstwe"""
        for i, number in enumerate(numbers):
            self._neurons[layer][i] = number

    def input_set_all(self, numbers):
        """This function fills input.

I do not know how yet. xD
        """
        self.layer_set_all(0, numbers)

    def input_get_all(self):
        """Returns some table of input numbers"""
        self.layer_get_all(0)

    def input_set_one(self, where, number):
        """Set one number in input."""
        self.layer_set_one(0, where, number)

    def input_get_one(self, where):
        """ygrdfgtr"""
        self.layer_get_one(0, where)

    def calculate(self):
        """Calculate output from network with actual input."""
        # first, do some checks that we can calculate
        # i will do it later xD
        def one_addition(self, in_layer, in_neuron, out_neuron):
            func = self._layer_functions[in_layer]
            if in_neuron == len(self._neurons[in_layer]):
                addition = 1.0
            else:
                addition = self._neurons[in_layer][in_neuron]
                if callable(func):
                    addition = func(addition)
            addition = addition * connections.get_connection_index(in_neuron, \
                out_neuron, len(self._neurons[in_layer]))
            return addition

        def one_layer(self, in_layer):
            for j in range(len(self._neurons[in_layer + 1])):
                value = 0.0
                for i in range(len(self._neurons[in_layer]) + 1):
                    # + 1 because of bias
                    value = value + one_addition(self, in_layer, i, j)
                self._neurons[in_layer + 1][j] = value

        for i in range(self._number_of_layers - 1):
            one_layer(self, i)

    def propagate_back(self, wanted_output):
        """This function makes network to learn using calculated output and
wanted output.
        """

    def output_get_one(self, where):
        """ This function read one indexed value from output."""
        self.layer_get_one(self._number_of_layers - 1, where)

    def output_get_all(self):
        """ Whis function reads output."""
        self.layer_get_all(self._number_of_layers - 1)
