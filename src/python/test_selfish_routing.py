import unittest
from selfish_routing import MoranProcess
import numpy as np


class TestMoranProcess(unittest.TestCase):

    def test_invariable_population_size(self):
        population_array=[2, 3, 5, 0]
        pop_size = sum(population_array)
        mp = MoranProcess(number_of_players=2, w=5, mutation_probability=0.001, population_array=[2, 3, 5, 0], seed=123)
        for i in range(10000):
            mp.step()
            self.assertTrue(pop_size == np.sum(mp.population))
            self.assertTrue(np.all(mp.population >=0))

    #def test_payoff_generation(self):





