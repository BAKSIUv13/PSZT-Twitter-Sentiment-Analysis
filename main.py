"""Main

Main script

"""

from network import network

print(5+6+7)

print(not isinstance(3, int))



NET = network.NeuralNetwork()


NET.set_number_of_layers(3)
NET.set_layer_size(0, 10)
NET.set_layer_size(1, 15)
NET.set_layer_size(2, 3)
NET.init_with_zeros()
for i in range(NET._number_of_layers):
    print(NET.layer_get_all(i))
NET.randomize_weights(-1, 1)
NET.input_set_all([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
for i in range(NET._number_of_layers):
    print(NET.layer_get_all(i))
NET.calculate()
for i in range(NET._number_of_layers):
    print(NET.layer_get_all(i))
NET.calculate()
for i in range(NET._number_of_layers):
    print(NET.layer_get_all(i))
