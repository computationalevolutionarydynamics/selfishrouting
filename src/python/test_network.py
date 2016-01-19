import unittest
from network import Network
import networkx as nx


class TestNetwork(unittest.TestCase):

    def test_Braess_network(self):
        t1 = self.createBraessNetwork()
        t1.enumerate_strategies_and_payoffs(2)
        self.assertTrue(True)

        #nx.draw(self.graph)
        #plt.show()
