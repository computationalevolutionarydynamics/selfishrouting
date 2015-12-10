
import numpy as np


class MoranProcess:

    def __init__(self, number_of_strategies, population_size, a, b, c, d, w):  # removed initial_population add intensity of selection

        """
        This function initialises different instance variables.
        :param number_of_strategies:
        :param population_size:
        :param a:
        :param b:
        :param c:
        :param d:
        :param w:
        :return:
        """

        assert population_size >= 2 , "Population should be larger than 1"
        self.number_of_strategies = number_of_strategies
        self.population_size = population_size
        self.population = np.array([])
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.w = w

    def generate_population(self): # generates a random population

        """
        This function generates an array for different values. Array length is equal to the population size specified
         in the init function. Differnt types of values in the array is equal to the number of stategies.
        :return:
        """
        i = 0
        while i < self.population_size:
            gen_ran_num = np.random.randint(1, self.number_of_strategies + 1, 1)  # generates a random number with equal probablity
            self.population = np.append(self.population, gen_ran_num)
            i += 1

    def __compute_payoff(self):
        # calculate number of differnt types in population
        self.sum_of_ones = 0
        self.sum_of_tows = 0
        for i in range(len(self.population)):
            if self.population[i] == 1:
                self.sum_of_ones += 1
            else:
                self.sum_of_tows += 1

        temp_a1 = ((self.sum_of_ones - 1 ) * self.a) / (self.population_size - 1)
        temp_a2 = ((self.sum_of_tows ) * self.b) / (self.population_size - 1)
        payoff_of_a = temp_a1 + temp_a2

        temp_b1 = ((self.sum_of_ones) * self.c) / (self.population_size - 1)
        temp_b2 = ((self.sum_of_tows - 1) * self.d ) / (self.population_size - 1)
        payoff_of_b = temp_b1 + temp_b2

        l1 = [payoff_of_a, payoff_of_b]
        return l1


    def __compute_fitness (self):
        #calculate transition from payoff to fitness
        payoff = self.__compute_payoff()
        temp_factor = self.w * payoff
        transition_factors_for_one = np.exp(temp_factor[1])
        transition_factors_for_two = np.exp(temp_factor[2])
        fitness_of_one = (self.sum_of_ones * transition_factors_for_one) / ((self.sum_of_ones * transition_factors_for_one) + (self.sum_of_tows * transition_factors_for_two))
        fitness_of_two = (self.sum_of_ones * transition_factors_for_two) / ((self.sum_of_ones * transition_factors_for_one) + (self.sum_of_tows * transition_factors_for_two))
        l1 = [fitness_of_one, fitness_of_two]
        return l1

    def __to_reproduce (self):
        fitness = self.__compute_fitness()
        if fitness[0] > fitness[1]:
            reproduce = 1
        elif fitness[0] < fitness[1]:
            reproduce = 2
        else:
            reproduce = np.random.randint(1, 3, 1)

        return reproduce

    def __replace (self):
        to_add = self.__to_reproduce()
        self.population = np.append(self.population, to_add)

    def __to_die_and_replace (self):
        num_to_die = np.random.randint(1, self.number_of_strategies + 1, 1)  # generates a random number with equal probablity
        self.population = np.delete(self.population, num_to_die)

    def __mutate (self):
        return


    def step(self):

        #generate population
        #self.__generate_population()
        print("Initial population")
        print (self.population)
        #print("\n")

        # select randomly an individual to die
        print("Individual selected and died")
        self.__to_die_and_replace()
        print("Population after the death")
        print (self.population)
        #print("\n")

        # compute fitness
        #fitness = self.__compute_fitness()
        #print("The fitness factors are")
        #print(fitness)
        #print("\n")

        # select randomly an individual to reproduce (fitness proportional)
        self.__replace()
        print("Individual reproduced based upon the fitness function")
        print(self.population)
        print("\n")

        # replace, maybe mutation

test = MoranProcess(2,10,1,2,3,4,5)
test.generate_population()

for i in range(1,10):
    test.step()








