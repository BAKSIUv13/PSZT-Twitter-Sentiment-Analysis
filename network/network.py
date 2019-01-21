"""This module contains class of network."""

from random import uniform
from enum import IntEnum

def cost(y_got, y_wanted):
    """This function calculates the cost."""
    return 0.5 * (y_got - y_wanted)**2

def cost_derivative(y_got, y_wanted):
    """Derivative of the cost. xD Nobody expected the derivative."""
    return y_got - y_wanted

def connection_index(in_neuron, out_neuron, in_layer_size):
    """ This functions calculates number of index of connection"""
    #
    # Indices are from 0 to 'size of layer' - 1. The 'size of layer'
    # is the bias.
    #
    return in_neuron + (in_layer_size + 1) * out_neuron

def neuron_indices(index, in_layer_size):
    """This function calculates indices of neurons in layers from index
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

class NeuralNetwork:
    """
    This is class which stores all information about the network
    and has its state.
    """

    def __init__(self):
        self._number_of_layers = None
        self._layer_sizes = None
        self._layer_functions = None
        self._layer_derivatives = None
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

    def get_number_of_layers(self):
        """This method returns number of layers in network."""
        self.check_level(NetworkSetupLevel.LAYERS_NUMBER)
        return self._number_of_layers

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

    def _func(self, in_layer, param):
        function = self._layer_functions[in_layer]
        if callable(function):
            return function(param)
        return param

    def _derivative(self, in_layer, param):
        function = self._layer_derivatives[in_layer]
        if callable(function):
            return function(param)
        return 1.0

    def randomize_weights(self, min_value, max_value):
        """Randomizes all weights in all connections and biases."""
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

    def connection_get(self, in_layer, index):
        """Returns value of connection at given index."""
        self.check_level(NetworkSetupLevel.READY)
        return self._connections[in_layer][index]

    def connection_set(self, in_layer, index, value):
        """Sets the value of the connection at given index."""
        self.check_level(NetworkSetupLevel.READY)
        self._connections[in_layer][index] = value

    def serialize_weights(self):
        """This function makes a list of weights of connections.

This list can be saved to file.
        """
        self.check_level(NetworkSetupLevel.READY)
        length = 0
        for connection_layer in self._connections:
            length = length + len(connection_layer)
        the_list = [0.0] * length
        index = 0
        for _, connection_layer in enumerate(self._connections):
            for _, connection in enumerate(connection_layer):
                the_list[index] = connection
                index = index + 1
        return the_list

    def paste_serialized_weights(self, weights):
        """This functions sets all connections from a list."""
        self.check_level(NetworkSetupLevel.READY)
        index = 0
        for _, connection_layer in enumerate(self._connections):
            for j, _ in enumerate(connection_layer):
                connection_layer[j] = weights[index]
                index = index + 1

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

    def feed(self):
        """Calculate output from network with actual input."""
        def weight(self, in_layer, in_neuron, out_neuron):
            return self._connections[in_layer][connection_index(in_neuron,\
                out_neuron, len(self._neurons[in_layer]))]

        def one_addition(self, in_layer, in_neuron, out_neuron):
            if in_neuron == len(self._neurons[in_layer]):
                addition = 1.0
            else:
                addition = self._neurons[in_layer][in_neuron]
                addition = self._func(in_layer, addition)
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

    def output_get_one(self, where):
        """ This function read one indexed value from output."""
        return self.layer_get_one(self._number_of_layers - 1, where)

    def output_get_all(self):
        """ Whis function reads output."""
        return self.layer_get_all(self._number_of_layers - 1)

    def copy_weights(self):
        """This function copies actual state of weights."""
        self.check_level(NetworkSetupLevel.READY)
        weights = []
        for i, layer in enumerate(self._connections):
            weights.append([])
            for _, value in enumerate(layer):
                weights[i].append(value)
        return weights

    def paste_weights(self, weights):
        """This function sets values of all weights"""
        self.check_level(NetworkSetupLevel.READY)
        for i, layer in enumerate(weights):
            for j, value in enumerate(layer):
                self._connections[i][j] = value

    def propagate_back(self, wanted_output):
        """This functions calculates gradient of actual state and given wanted
output.

Output of this function can be used to calculate average gradient and next it
can be used to learn this network.
"""
        self.check_level(NetworkSetupLevel.READY)
        return self._propagate_gradient(wanted_output)

    def _create_empty_gradient(self):
        """This function creates a zero gradient for other functions"""
        number_of_layers = self._number_of_layers
        number_of_passes = number_of_layers - 1
        gradient = [None] * number_of_passes
        for i, _ in enumerate(gradient):
            gradient[i] = [0.0] * len(self._connections[i])
        return gradient

    def create_empty_gradient(self):
        """Returns zero gradient"""
        self.check_level(NetworkSetupLevel.READY)
        return self._create_empty_gradient()

    def _propagate_gradient(self, wanted_output):
        """This functions calculates gradient of actual state and given wanted
output."""
        number_of_layers = self._number_of_layers
        last_layer_index = number_of_layers - 1
        last_pass_index = number_of_layers - 2
        neurons = self._neurons

        grad = self._create_empty_gradient()
        temp_layer_l = [] # Used to store multiplied values
        temp_layer_r = [] # It is the same thing, but from earlier layers
        # Right temporary layer stores the sum of all derivatives of cost over
        # all connections on the right side of responding neuron.

        for i, out_neuron_value in enumerate(neurons[last_layer_index]):
            temp_layer_r.append(\
                cost_derivative(out_neuron_value, wanted_output[i]))
        # Here we set needed values in right temp layer that will be used later.

        for layer in range(last_pass_index, -1, -1):
            temp_layer_l = [0.0] * len(neurons[layer])
            layer_size = self._layer_sizes[layer]
            for r_index, r_value in enumerate(temp_layer_r):
                # Now I have something on the right side and I completely don't
                # care about others.
                for l_index, l_value in enumerate(neurons[layer]):
                    to_layer = r_value * self._derivative(layer, l_value) \
                        * self._connections\
                        [layer]\
                        [connection_index(l_index, r_index, layer_size)]
                    to_neuron = r_value * self._func(layer, l_value)
                    temp_layer_l[l_index] += to_layer
                    grad[layer][connection_index(l_index, r_index, layer_size)]\
                        = to_neuron
                # bias:    xD
                grad\
                    [layer]\
                    [\
                        connection_index(len(neurons[layer]),\
                        r_index,\
                        layer_size)\
                        ] = r_value # * 1.0

            temp_layer_r = temp_layer_l
        return grad

    def get_calculation(self, input_values):
        """Short form of calculating network."""
        self.input_set_all(input_values)
        self.feed()
        return self.output_get_all()

    def learn(self, input_sets, expectations, gradient_multiplier):
        """Function that lears our network."""
        calculated_gradients = []
        for i, in_set in enumerate(input_sets):
            self.input_set_all(in_set)
            self.feed()
            calculated_gradients.append(self.propagate_back(expectations[i]))
        gradient = merge_weight_sets(\
            calculated_gradients,\
            - gradient_multiplier / len(input_sets)
            )
        gradient = merge_weight_sets(\
            [gradient, self.copy_weights()],\
            1.0
            )
        self.paste_weights(gradient)

def merge_weight_sets(sets, multiplier):
    """Function that merges multiple weight or gradient sets and multiplies
them by some number."""
    final_set = []
    for layer in sets[0]:
        final_set.append(layer.copy())
    for i in range(1, len(sets)):
        for j, layer in enumerate(sets[i]):
            for k, value in enumerate(layer):
                final_set[j][k] += value
    for _, layer in enumerate(final_set):
        for i, _ in enumerate(layer):
            layer[i] *= multiplier
    return final_set
