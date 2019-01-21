"""This module contains useful functions that use network so we can write
less."""

#import network

def calculate(net, input_set):
    """This function feeds the network and returns its output."""
    return net.get_calculation(input_set)

def full_learning(
        net,
        input_sets,
        expectations,
        speed,
        iterations_quantity
        ):
    """This function does a loop that teaches our network with given set."""
    for i in range(iterations_quantity):
        net.learn(input_sets, expectations, speed)
        meh = net.look_for_nans()
        if meh:
            print("Found nan in {:5d} iteration:(".format(i))
            for where in meh:
                print(where)
            return
        if i % 100 == 0:
            print("Learning: {:5} iterations passed.".format(i))

def load_from_file(
        net,
        file_path
        ):
    """This function load entire weight vector to network from file."""
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
