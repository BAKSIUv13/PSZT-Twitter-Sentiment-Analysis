"""This module contains class of network."""

from random import uniform
from enum import IntEnum

def get_connection_index(in_neuron, out_neuron, in_layer_size):
    """ This functions calculates number of index of connection"""
    #
    # Indices are from 0 to 'size of layer' - 1. The 'size of layer' is the bias.
    #
    return in_neuron + (in_layer_size + 1) * out_neuron

def get_neuron_indices(index, in_layer_size):
    """This function calculates number of neurons in layers from index
of connection.
"""
    return (index % (in_layer_size + 1), index / (in_layer_size + 1))

def number_of_connections(in_layer_size, out_layer_size):
    """Returns number of connections between layers including bias."""
    return in_layer_size * out_layer_size + out_layer_size


class NetworkSetupLevel(IntEnum):
    """Enumeration of levels of settings of neural network.

These levels are used to check if network is set and can be used from outside,
too.
"""
    BLANK = - 1
        # The network has no anything set.
    LAYERS_NUMBER = 0
        # There is number of layers. Each layer may have size set,
        # but it don't have to.
    READY = 1
        # All layers have sizes and connections are made. Network is ready to
        # work.
    FILLED = 2
        # I don't know if we need it.
    #def __str__(self):
    #    return self.value


class NeuralNetwork:
    """
    This is class which stores all information about the network
    and has its state.
    """

    def __init__(self):
        self._number_of_layers = None
        self._layer_sizes = None
        self._layer_functions = None
        self._layer_derivatives = None # hmm... it is only sugestion now
        self._neurons = None
        self._connections = None
        self._setup_level = NetworkSetupLevel.BLANK

    def check_level(self, level):
        """Check that setup level is sush or greater."""
        if self._setup_level < level:
            raise ValueError("expected network setup level "
                             + str(level)
                             + " or greater, got "
                             + str(self._setup_level))


    def clear_totally(self):
        """ This method erares all data of network."""
        self._number_of_layers = None
        self._layer_sizes = None
        self._layer_functions = None
        self._layer_derivatives = None
        self._neurons = None
        self._connections = None
        self._setup_level = NetworkSetupLevel.BLANK

    def set_number_of_layers(self, number):
        """This method sets number of layers in network."""
        if not isinstance(number, int) or number < 1:
            raise ValueError("expected positive int")
        self._neurons = None
        self._connections = None
        self._number_of_layers = number
        self._layer_sizes = [0] * number
        self._layer_functions = [None] * (number - 1)
        self._layer_derivatives = [None] * (number - 1)
        self._neurons = [None] * number
        self._connections = [None] * (number - 1)
        self._setup_level = NetworkSetupLevel.LAYERS_NUMBER
        # Connections are numbered is way that 0 means after 0 layer.

    def set_layer_size(self, which_layer, size):
        """This method sets quantity of neurons in indexed layer.

Layer 0 is input. Layer number - 1 is the output.
        """
        if not isinstance(which_layer, int):
            raise ValueError("expected 'which_layer' "
                             + "as an int")
        if not isinstance(size, int):
            raise ValueError("expected 'size' as an int")
        if which_layer < 0 or which_layer >= self._number_of_layers:
            raise ValueError("'which_layer' has to be in [0,"
                             + str(self._number_of_layers)
                             + ")")
        if size < 1:
            raise ValueError("expected 'which_layer' as an positive int")

        self.check_level(NetworkSetupLevel.LAYERS_NUMBER)

        self._layer_sizes[which_layer] = size
        self._neurons[which_layer] = [0.0] * size

    def get_layer_size(self, which_layer):
        """This function returns size of picked layer.

If the layer has not its size set or it can't even have the size, exception is
thrown.
"""
        if not isinstance(which_layer, int):
            raise ValueError("expected 'which_layer' as an int")
        self.check_level(NetworkSetupLevel.LAYERS_NUMBER)
        if which_layer < 0 or which_layer >= self._number_of_layers:
            raise ValueError("'which_layer' has to be in [0,"
                             + self._number_of_layers
                             + ")")
        size = self._layer_sizes[which_layer]
        if isinstance(size, int):
            return size
        raise ValueError("size of layer " + which_layer + "is not set")

    def init_with_zeros(self):
        """This function shall create the neurons and their connections
and everything that is necessary this network to work.
        """
        self.check_level(NetworkSetupLevel.LAYERS_NUMBER)
        for i in range(self._number_of_layers):
            self.get_layer_size(i) # We check if this size is set.
        for layer in self._neurons:
            for j, _ in enumerate(layer):
                layer[j] = 0.0
        for i in range(self._number_of_layers - 1):
            self._connections[i] = [0.0] \
                * number_of_connections(self._layer_sizes[i], \
                self._layer_sizes[i + 1])
        self._setup_level = NetworkSetupLevel.READY

    def set_function(self, which_layer, func):
        """This function is to set the function between layer 'layer' and next.

This is not finished. Here I need to add derivatires somehow and I
don't know how. It is temporary.

Layer means destination layer index + 1

If function is not set this layer will be treated as linear (f(x)=x).
        """
        if ~callable(func):
            raise ValueError("expected 'func' as a function")
        self.check_level(NetworkSetupLevel.LAYERS_NUMBER)
        self._layer_functions[which_layer] = func

    def set_derivative(self, which_layer, func):
        """This function is to set the derivative between layer 'layer'
and next.

Layer means destination layer index + 1

If function is not set this layer will be treated as const (f(x)=1).
        """
        if ~callable(func):
            raise ValueError("expected 'func' as a function")
        self.check_level(NetworkSetupLevel.LAYERS_NUMBER)
        self._layer_derivatives[which_layer] = func

    def randomize_weights(self, min_value, max_value):
        """This function randomizes all weights in all connections and biases.
        """
        #if not isinstance(min_value, (float, int)) \
        #        or not isinstance(max_value, (float, int)):
        #    raise ValueError("expected 'min_value' and "
        #                     + "'max_value' as floats or ints")
        #if min_value > max_value:
        #    raise ValueError("expected "
        #                     + "min_value <= max_value")
        self.check_level(NetworkSetupLevel.READY)
        for i in range(self._number_of_layers - 1):
            for j in range(len(self._connections[i])):
                self._connections[i][j] = uniform(min_value, max_value)

    def layer_get_one(self, layer, where):
        """Returns value stored by indicated neuron"""
        self.check_level(NetworkSetupLevel.READY)
        return self._neurons[layer][where]

    def layer_set_one(self, layer, where, number):
        """Sets value of indicated neuron"""
        self.check_level(NetworkSetupLevel.READY)
        self._neurons[layer, where] = number

    def layer_get_all(self, layer):
        """Returns values of neurons in whole layer."""
        self.check_level(NetworkSetupLevel.READY)
        return self._neurons[layer].copy()

    def layer_set_all(self, layer, numbers):
        """Sets values in layer."""
        self.check_level(NetworkSetupLevel.READY)
        for i, number in enumerate(numbers):
            self._neurons[layer][i] = number

    def input_set_all(self, numbers):
        """This function fills input."""
        self.layer_set_all(0, numbers)

    def input_get_all(self):
        """Returns table of input numbers"""
        self.layer_get_all(0)

    def input_set_one(self, where, number):
        """Set one number in input."""
        self.layer_set_one(0, where, number)

    def input_get_one(self, where):
        """Returns number in input layer."""
        self.layer_get_one(0, where)

    def calculate(self):
        """Calculate output from network with actual input."""
        def weight(self, in_layer, in_neuron, out_neuron):
            return self._connections[in_layer][get_connection_index(in_neuron,\
                out_neuron, len(self._neurons[in_layer]))]

        def one_addition(self, in_layer, in_neuron, out_neuron):
            func = self._layer_functions[in_layer]
            if in_neuron == len(self._neurons[in_layer]):
                addition = 1.0
            else:
                addition = self._neurons[in_layer][in_neuron]
                if callable(func):
                    addition = func(addition)
            addition = addition * weight(self, in_layer, in_neuron, out_neuron)
            return addition

        def one_layer(self, in_layer):
            for j in range(len(self._neurons[in_layer + 1])):
                value = 0.0
                for i in range(len(self._neurons[in_layer]) + 1):
                    # + 1 because of bias
                    value = value + one_addition(self, in_layer, i, j)
                self._neurons[in_layer + 1][j] = value

        self.check_level(NetworkSetupLevel.READY)
        for i in range(self._number_of_layers - 1):
            one_layer(self, i)

    def propagate_back(self, wanted_output):
        """This function makes network to learn using calculated output and
wanted output.
        """
        self.check_level(NetworkSetupLevel.READY)
        wanted_output = 1
        wanted_output = wanted_output + 1

    def output_get_one(self, where):
        """ This function read one indexed value from output."""
        return self.layer_get_one(self._number_of_layers - 1, where)

    def output_get_all(self):
        """ Whis function reads output."""
        print(self._number_of_layers - 1)
        return self.layer_get_all(self._number_of_layers - 1)
