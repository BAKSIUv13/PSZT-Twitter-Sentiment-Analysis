"""This module contains functions that calculates indices of connections"""
#
# Indices are from 0 to 'size of layer' - 1. The 'size of layer' is the bias.
#
#
#
#
def get_connetions_index(in_layer, out_layer, in_layer_size):
    """ This functions calculates number of index of connection"""
    return in_layer + (in_layer_size + 1) * out_layer

def get_neuron_indices(index, in_layer_size):
    """saddsadsaads"""
    return (index % (in_layer_size + 1), index / (in_layer_size + 1))
