"""Main

Almost main script

"""

from network import network

print(5+6+7)

#print(not isinstance(3, int))

CI = network.connection_index

SPEED = 0.01

ITERATIONS = 100

IN_SET_1 = [0.1, 3.2, 0.5]
IN_SET_2 = [6.3, 0.0, -3.0]
IN_SET_3 = [0.15, 3.33, 0.6]
OUT_SET_1 = [1.0, 3.3]
OUT_SET_2 = [0.0, -0.45]

print("Start test of learning with speed = {:3.3f} and {:3d} iterations."\
      .format(SPEED, ITERATIONS))

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
#for i in range(NET.get_number_of_layers()):
#    print(NET.layer_get_all(i))

NET.paste_serialized_weights(QWE)

#NET.randomize_weights(-1, 0)
#NET.connection_set(1, CI(5, 0, 5), 2.0)
#QWE = NET.serialize_weights()

#NET.input_set_all([0.1, 3.2, 0.5])#, 0., 0., 0., 0., 0., 0., 0.])
#for i in range(NET.get_number_of_layers()):
#    print(NET.layer_get_all(i))
#NET.feed()
#for i in range(NET.get_number_of_layers()):
#    print(NET.layer_get_all(i))

NET.input_set_all(IN_SET_1)
NET.feed()
print(NET.output_get_all())

NET.input_set_all(IN_SET_2)
NET.feed()
print(NET.output_get_all())

NET.input_set_all(IN_SET_3)
NET.feed()
print(NET.output_get_all())

for i in range(ITERATIONS):
    NET.learn([IN_SET_1, IN_SET_2], [OUT_SET_1, OUT_SET_2], SPEED)


NET.input_set_all(IN_SET_1)
NET.feed()
print(NET.output_get_all())

NET.input_set_all(IN_SET_2)
NET.feed()
print(NET.output_get_all())

NET.input_set_all(IN_SET_3)
NET.feed()
print(NET.output_get_all())

#print("======")

#print(QWE)

#with open('file.txt', 'w') as filee:
#    filee.writelines("%s\n" % number for number in QWE)
