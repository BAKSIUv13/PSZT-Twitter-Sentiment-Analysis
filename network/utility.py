"""This module contains useful functions that use network so we can write
less."""

#import network

def calculate(net, input_set):
    """This function feeds the network and returns its output."""
    net.input_set_all(input_set)
    net.feed()
    return net.output_get_all()

def full_learning(
        net,
        input_sets,
        expectations,
        speed,
        iterations_quantity
        ):
    """This function fires a loop that teaches our network with given set."""
    for _ in range(iterations_quantity):
        net.learn(input_sets, expectations, speed)

def load_from_file(
        net,
        file_path
        ):
    """This function load enitire weight vector to network from file."""
    serialized = []
    with open(file_path, 'r') as the_file:
        file_content = the_file.readlines()
    for line in file_content:
        curr = line[:-1]
        serialized.append(float(curr))
    net.paste_serialized_weights(serialized)

def save_to_file(
        net,
        file_path
        ):
    """This function saves state of the network (only weight values)
to file."""
    serialized = net.serialize_weights()
    with open(file_path, 'w') as the_file:
        the_file.writelines("%s\n" % number for number in serialized)
