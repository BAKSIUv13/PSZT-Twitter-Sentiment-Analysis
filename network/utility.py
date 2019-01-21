"""This module contains useful functions that use network so we can write
less."""

#import network

def calculate(net, input_set):
    """This function feeds the network and returns its output."""
    net.input_set_all(input_set)
    net.feed()
    return net.output_get_all()

def fgh():
    pass