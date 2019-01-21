"""Main

Almost main script

"""

import math

from network import network
from network import utility as u

print(5+6+7)

#print(not isinstance(3, int))

CI = network.connection_index

SPEED = 0.00315

ITERATIONS = 8000

def hidden_func(argus):
    """Function"""
    return math.atan(argus)
    #if argus > 0.0:
    #    return argus
    #return 0.0

def hidden_derivative(argus):
    """Function derivative."""
    return 1.0 / (argus**2 + 1.0)
    #if argus > 0.0:
    #    return 1.0
    #return 0.0

IN_SET_1 = [0.1, 3.2, 0.5]
IN_SET_2 = [6.3, 0.0, -3.0]
IN_SET_3 = [0.55, 4.33, 0.6]
IN_SET_4 = [0.0, 0.0, -0.5]
OUT_SET_1 = [1.0, 3.3]
OUT_SET_2 = [0.0, -0.45]
OUT_SET_3 = [0.7, 0.65]
OUT_SET_4 = [0.0, 0.45]

print("Start test of learning with speed = {:3.3f} and {:3d} iterations."\
      .format(SPEED, ITERATIONS))

'''
QWE = []

with open('file.txt', 'r') as filee:
    FILE_CONTENT = filee.readlines()
    for line in FILE_CONTENT:
        curr = line[:-1]

        QWE.append(float(curr))

print(QWE)
'''


NET = network.NeuralNetwork()


NET.set_number_of_layers(6)
NET.set_layer_size(0, 3)
NET.set_layer_size(1, 6)
NET.set_layer_size(2, 8)
NET.set_layer_size(3, 6)
NET.set_layer_size(4, 5)
NET.set_layer_size(5, 2)

NET.set_function(0, hidden_func)
NET.set_derivative(0, hidden_derivative)

NET.set_function(1, hidden_func)
NET.set_derivative(1, hidden_derivative)

NET.set_function(2, hidden_func)
NET.set_derivative(2, hidden_derivative)

NET.set_function(3, hidden_func)
NET.set_derivative(3, hidden_derivative)

NET.set_function(4, hidden_func)
NET.set_derivative(4, hidden_derivative)

NET.init_with_zeros()
#for i in range(NET.get_number_of_layers()):
#    print(NET.layer_get_all(i))

#NET.paste_serialized_weights(QWE)

NET.randomize_weights(-1.0, 1.0)
#NET.connection_set(1, CI(5, 0, 5), 2.0)
#QWE = NET.serialize_weights()

#NET.input_set_all([0.1, 3.2, 0.5])#, 0., 0., 0., 0., 0., 0., 0.])
#for i in range(NET.get_number_of_layers()):
#    print(NET.layer_get_all(i))
#NET.feed()
#for i in range(NET.get_number_of_layers()):
#    print(NET.layer_get_all(i))


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


#print("======")

#print(QWE)

#with open('file.txt', 'w') as filee:
#    filee.writelines("%s\n" % number for number in QWE)
