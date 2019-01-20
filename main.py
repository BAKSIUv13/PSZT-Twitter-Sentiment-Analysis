"""Main

Main script

"""

from network import network
#ci = network.connection_index

print(5+6+7)

print(not isinstance(3, int))

CI = network.connection_index


QWE = []

with open('file.txt', 'r') as filee:
    FILE_CONTENT = filee.readlines()
    for line in FILE_CONTENT:
        curr = line[:-1]

        QWE.append(float(curr))

print(QWE)


NET = network.NeuralNetwork()


NET.set_number_of_layers(3)
NET.set_layer_size(0, 3)
NET.set_layer_size(1, 5)
NET.set_layer_size(2, 2)
NET.init_with_zeros()
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))

NET.paste_weights(QWE)

#NET.randomize_weights(-1, 0)
#NET.connection_set(1, CI(5, 0, 5), 2.0)
#QWE = NET.serialize_weights()

NET.input_set_all([0., 0., 0.])#, 0., 0., 0., 0., 0., 0., 0.])
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))
NET.calculate()
for i in range(NET.get_number_of_layers()):
    print(NET.layer_get_all(i))

print("======")

print(QWE)

FILE = 0

#with open('file.txt', 'w') as filee:
#    filee.writelines("%s\n" % number for number in QWE)
