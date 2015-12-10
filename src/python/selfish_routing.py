import numpy as np


class MoranProcess:
    def __init__(self, number_of_strategies, population_size, a, b, c, d,
                 w):  # removed initial_population add intensity of selection

        """
        This function initialises different instance variables.
        :param number_of_strategies:
        :param population_size:
        :param a: a from the payoff matrix (a, b; c, d)
        :param b: b from the payoff matrix (a, b; c, d)
        :param c: c from the payoff matrix (a, b; c, d)
        :param d: d from the payoff matrix (a, b; c, d)
        :param w: intensity of selection
        :return:
        """

        assert population_size >= 2, "Population should be larger than 1"
        self.number_of_strategies = number_of_strategies
        self.population_size = population_size
        self.population = np.array([])
        self.generate_population()
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.w = w


    def generate_population(self):  # generates a random population

        """
        This function generates an array for different values. Array length is equal to the population size specified
         in the init function. Differnt types of values in the array is equal to the number of stategies.
        :return:
        """
        i = 0
        while i < self.population_size:
            gen_ran_num = np.random.randint(1, self.number_of_strategies + 1,
                                            1)  # generates a random number with equal probablity
            self.population = np.append(self.population, gen_ran_num)
            i += 1

    def __compute_payoff(self):
        """
        We need some more detailed comments here... mayvbe...
        :return:
        """
        self.number_of_players_type_1 = len(np.where(self.population == 1))
        self.number_of_players_type_2 = len(np.where(self.population == 2))

        temp_a1 = ((self.number_of_players_type_1 - 1) * self.a) / (self.population_size - 1)
        temp_a2 = (self.number_of_players_type_2 * self.b) / (self.population_size - 1)
        payoff_of_a = temp_a1 + temp_a2

        temp_b1 = (self.number_of_players_type_1 * self.c) / (self.population_size - 1)
        temp_b2 = ((self.number_of_players_type_2 - 1) * self.d) / (self.population_size - 1)
        payoff_of_b = temp_b1 + temp_b2

        return payoff_of_a, payoff_of_b

    def __compute_fitness(self):
        # calculate transition from payoff to fitness
        payoff_a, payoff_b = self.__compute_payoff()
        transition_factors_for_one = np.exp(self.w*payoff_a)
        transition_factors_for_two = np.exp(self.w*payoff_b)
        fitness_of_one = (self.number_of_players_type_1 * transition_factors_for_one) / (
        (self.number_of_players_type_1 * transition_factors_for_one) + (
         self.number_of_players_type_2 * transition_factors_for_two))
        fitness_of_two = (self.number_of_players_type_1 * transition_factors_for_two) / (
        (self.number_of_players_type_1 * transition_factors_for_one) + (
         self.number_of_players_type_2 * transition_factors_for_two))
        return fitness_of_one, fitness_of_two

    def __replace(self):
        to_add = np.random.choice([1, 2], p= self.__compute_fitness())
        self.population = np.append(self.population, to_add)

    def __to_die_and_replace(self):
        num_to_die = np.random.randint(1, self.number_of_strategies + 1,
                                       1)  # generates a random number with equal probablity
        self.population = np.delete(self.population, num_to_die)

    def __mutate(self):
        pass

    def step(self):

        # generate population
        # self.__generate_population()
        print("Initial population")
        print(self.population)
        # print("\n")

        # select randomly an individual to die
        print("Individual selected and died")
        self.__to_die_and_replace()
        print("Population after the death")
        print(self.population)
        # print("\n")

        # compute fitness
        # fitness = self.__compute_fitness()
        # print("The fitness factors are")
        # print(fitness)
        # print("\n")

        # select randomly an individual to reproduce (fitness proportional)
        self.__replace()
        print("Individual reproduced based upon the fitness function")
        print(self.population)
        print("\n")

        # replace, maybe mutation

