"""Unit tests for network module."""
import unittest

from network import network

class TestNeuralNetwork(unittest.TestCase):
    """."""
    def setUp(self):
        """."""
        self.net = network.NeuralNetwork()

    def test_layer_number(self):
        """."""
        self.net.set_number_of_layers(3)
        self.assertEqual(self.net.get_number_of_layers(), 3)
        self.net.check_level(network.NetworkSetupLevel.LAYERS_NUMBER)

    def test_fill_zeros(self):
        """."""
        self.net.set_number_of_layers(3)
        self.net.set_layer_size(0, 100)
        self.net.set_layer_size(1, 45)
        self.net.set_layer_size(2, 2)
        self.assertEqual(self.net.get_layer_size(0), 100)
        self.assertEqual(self.net.get_layer_size(1), 45)
        self.assertEqual(self.net.get_layer_size(2), 2)
        self.net.init_with_zeros()
        self.assertEqual(self.net.layer_get_one(1, 36), 0.0)

if __name__ == '__main__':
    unittest.main()
