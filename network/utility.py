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
