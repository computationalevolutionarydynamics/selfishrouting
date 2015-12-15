import unittest
from selfish_routing import MoranProcess
import numpy as np


class TestMoranProcess(unittest.TestCase):

    def test_invariable_population_size(self):
        game_matrix = np.random.randint(0, 100, 4).reshape(2,2)
        population_array=[60, 40]
        pop_size = sum(population_array)
        mp = MoranProcess(game_matrix, w=5, mutation_probability=0.001, population_array=[60, 40])
        for i in range(10000):
            mp.step()
            self.assertTrue(pop_size == np.sum(mp.population))
            self.assertTrue(np.all(mp.population >=0))



