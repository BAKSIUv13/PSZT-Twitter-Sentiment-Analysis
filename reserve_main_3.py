"""Main

Almost main script
"""

import math
from random import uniform

from network import network
from network import utility as u


SPEED = 0.005

ITERATIONS = 200

def hidden_func(argus):
    """Function"""
    return math.atan(argus)

def hidden_derivative(argus):
    """Function derivative."""
    return 1.0 / (argus**2 + 1.0)

IN_SET_1 = [0.0] * 280
IN_SET_2 = [0.0] * 280
IN_SET_3 = [0.0] * 280
IN_SET_4 = [0.0] * 280
OUT_SET_1 = [1.0, 3.3]
OUT_SET_2 = [0.0, -0.45]
OUT_SET_3 = [0.7, 0.65]
OUT_SET_4 = [0.0, 0.45]

for i in range(280):
    IN_SET_1[i] = uniform(0.0, 1.0)
    IN_SET_2[i] = uniform(0.0, 1.0)
    IN_SET_3[i] = uniform(0.0, 1.0)
    IN_SET_4[i] = uniform(0.0, 1.0)

print("Start test of learning with speed = {:.6f} and {:3d} iterations."\
      .format(SPEED, ITERATIONS))

NET = network.NeuralNetwork()

NET.set_number_of_layers(3)
NET.set_layer_size(0, 280)
NET.set_layer_size(1, 20)
NET.set_layer_size(2, 2)

NET.set_function(0, hidden_func)
NET.set_derivative(0, hidden_derivative)

NET.init_with_zeros()

NET.randomize_weights(-1.0, 1.0)

print(u.calculate(NET, IN_SET_1))
print(u.calculate(NET, IN_SET_2))
print(u.calculate(NET, IN_SET_3))
print(u.calculate(NET, IN_SET_4))

u.full_learning(
    NET,
    [IN_SET_1, IN_SET_2, IN_SET_3, IN_SET_4],
    [OUT_SET_1, OUT_SET_2, OUT_SET_3, OUT_SET_4],
    SPEED,
    ITERATIONS
    )


print(u.calculate(NET, IN_SET_1))
print(u.calculate(NET, IN_SET_2))
print(u.calculate(NET, IN_SET_3))
print(u.calculate(NET, IN_SET_4))


u.save_to_file(NET, 'pliczek2')
