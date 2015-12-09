
import numpy as np


class MoranProcess:

    def __init__(self, num_of_species, population_size):  # removed initial_population
        self.num_of_species = num_of_species
        self.population_size = population_size
        self.population = np.array([])

    def __generate_population(self): # generates a random population

        i = 0

        while i < self.population_size:
            gen_ran_num = np.random.randint(1, self.num_of_species + 1, 1)  # generates a random number with equal probablity
            self.population = np.append(self.population, gen_ran_num)
            i += 1

    def __compute_fitness (self):
        return

    def __to_reproduce (self):
        return

    def __to_die_and_replace (self):
        num_to_die = np.random.randint(1, self.num_of_species + 1, 1)  # generates a random number with equal probablity
        self.population = np.delete(self.population, num_to_die)

    def __mutate (self):
        return

    def __replace (self):
        return

    def step(self):

        #generate population
        self.__generate_population()
        print("Initial population \n")
        print (self.population)
        # compute fitness

        # select randomly an individual to reproduce (fitness proportional)

        # select randomly an individual to die
        print("Individual selected and died \n")
        self.__to_die_and_replace()
        print("Population after the death\n")
        print (self.population)
        # replace, maybe mutation


print("Hello world");
m1 = MoranProcess(3,10)
m1.step()




