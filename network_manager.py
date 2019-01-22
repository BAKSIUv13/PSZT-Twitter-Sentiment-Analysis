"""Module to use network exactly how it is needed in our final program.

This network has 3 layers. Their sizes are 280, 20, 2.
"""

import math

from network import network
from network import utility



NUMBER_OF_LAYERS = 3
LAYER_SIZES = [280, 20, 2]




def hidden_func(argus):
    """Function"""
    return math.atan(argus)

def hidden_derivative(argus):
    """Function derivative."""
    return 1.0 / (argus**2 + 1.0)





def create_zero_network():
    """Returns network with zeros in weights."""
    net = network.NeuralNetwork()
    net.set_number_of_layers(NUMBER_OF_LAYERS)
    for i, size in enumerate(LAYER_SIZES):
        net.set_layer_size(i, size)
    net.init_with_zeros()
    net.set_function(0, hidden_func)
    net.set_derivative(0, hidden_derivative)
    return net

def create_random_network(min_value, max_value):
    """Returns random weighted network."""
    net = create_zero_network()
    net.randomize_weights(min_value, max_value)
    return net

def load_network(file_path):
    """Returns network filled with weights from file."""
    net = create_zero_network()
    utility.load_from_file(net, file_path)
    return net
