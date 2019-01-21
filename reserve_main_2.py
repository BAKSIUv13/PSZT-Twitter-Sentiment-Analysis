"""Main

Almost main script
"""

import math

from network import network
from network import utility as u


def hidden_func(argus):
    """Function"""
    return math.atan(argus)

def hidden_derivative(argus):
    """Function derivative."""
    return 1.0 / (argus**2 + 1.0)

IN_SET_1 = [0.1, 3.2, 0.5]
IN_SET_2 = [6.3, 0.0, -3.0]
IN_SET_3 = [0.55, 4.33, 0.6]
IN_SET_4 = [0.0, 0.0, -0.5]
OUT_SET_1 = [1.0, 3.3]
OUT_SET_2 = [0.0, -0.45]
OUT_SET_3 = [0.7, 0.65]
OUT_SET_4 = [0.0, 0.45]

NET = network.NeuralNetwork()

NET.set_number_of_layers(3)
NET.set_layer_size(0, 3)
NET.set_layer_size(1, 20)
NET.set_layer_size(2, 2)

NET.set_function(0, hidden_func)
NET.set_derivative(0, hidden_derivative)

NET.init_with_zeros()

u.load_from_file(NET, 'pliczek')

print(u.calculate(NET, IN_SET_1))
print(u.calculate(NET, IN_SET_2))
print(u.calculate(NET, IN_SET_3))
print(u.calculate(NET, IN_SET_4))
