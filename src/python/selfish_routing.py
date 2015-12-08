
import numpy as np


class MoranProcess:

    def __init__(self, num_of_species, population_size):  # removed initial_population

        """
        :return:
        """
        i = 0
        self.population = np.array([])
        while (i < population_size):
            gen_ran_num = np.random.uniform(1, num_of_species, 1)  # generates a random number with equal probablity
            np.append(self.population, gen_ran_num)


    def __compute_fitness (self):
        return

    def __to_reproduce (self):
        return

    def __to_die (self):
        return

    def __mutate (self):
        return

    def __replace (self):
        return

    def step(self):

        var = self.population
        print (var)
        # compute fitness

        # select randomly an individual to reproduce (fitness proportional)

        # select randomly an individual to die

        # replace, maybe mutation


test = MoranProcess(3,10)
test.step()