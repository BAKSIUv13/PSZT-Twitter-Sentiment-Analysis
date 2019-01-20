"""Main

Main script

"""

from network import network
#ci = network.connection_index

print(5+6+7)

print(not isinstance(3, int))

ci = network.connection_index

NET = network.NeuralNetwork()


NET.set_number_of_layers(3)
NET.set_layer_size(0, 3)
NET.set_layer_size(1, 5)
NET.set_layer_size(2, 2)
NET.init_with_zeros()
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))
NET.randomize_weights(-1, 0)
NET.connection_set(1, ci(5, 0, 5), 2.0)
NET.input_set_all([0., 0., 0.])#, 0., 0., 0., 0., 0., 0., 0.])
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))
NET.calculate()
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))
NET.calculate()
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))
