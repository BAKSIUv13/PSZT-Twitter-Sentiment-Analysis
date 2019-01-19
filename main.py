"""Main

Main script

"""

from network import network

print(5+6+7)

NET = network.NeuralNetwork()


NET.set_number_of_layers(3)
NET.set_layer_size(0, 10)
NET.set_layer_size(1, 15)
NET.set_layer_size(2, 3)
NET.init_with_zeros()
NET.randomize_weights(0.0, 1.0)
NET.input_set_all([1., 0., 1., 0., 1., 0., 1., 0., 1., 0, 0, 0, 20, 302, 30, 201, 101, 0])
NET.calculate()
print(NET.output_get_all)
