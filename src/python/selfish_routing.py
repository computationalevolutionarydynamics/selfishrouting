import numpy as np


class MoranProcess:
    def __init__(self, a, b, c, d,
                 w, mutation_probability, population_array):  # removed initial_population add intensity of selection

        """
        This function initialises different instance variables.
        :param number_of_strategies:
        :param a: a from the payoff matrix (a, b; c, d)
        :param b: b from the payoff matrix (a, b; c, d)
        :param c: c from the payoff matrix (a, b; c, d)
        :param d: d from the payoff matrix (a, b; c, d)
        :param w: intensity of selection
        :param mutation_probability: mutation probability
        :param population_array: put some description here....
        :return:
        """
        # temporarily we only accept populations of two types
        assert len(population_array) == 2, "This works for two types only!"
        self.number_of_strategies = 2
        self.population = np.array(population_array, dtype=int)
        self.population_size = np.sum(self.population)
        assert self.population_size >= 2, "Population should be larger than 1"
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.w = w
        assert 0 <= mutation_probability <=1, "Mutation probability should be in [0, 1]"
        self.mutation_probability = mutation_probability


    def __compute_payoff(self):
        """
        We need some more detailed comments here... maybe...
        :return:
        """

        temp_a1 = ((self.population[0] - 1) * self.a) / (self.population_size - 1)
        temp_a2 = (self.population[1] * self.b) / (self.population_size - 1)
        payoff_of_a = temp_a1 + temp_a2

        temp_b1 = (self.population[0] * self.c) / (self.population_size - 1)
        temp_b2 = ((self.population[1] - 1) * self.d) / (self.population_size - 1)
        payoff_of_b = temp_b1 + temp_b2

        return payoff_of_a, payoff_of_b

    def __compute_fitness(self):
        # calculate transition from payoff to fitness
        payoff_a, payoff_b = self.__compute_payoff()
        transition_factors_for_one = np.exp(self.w*payoff_a)
        transition_factors_for_two = np.exp(self.w*payoff_b)
        fitness_of_one = (self.population[0] * transition_factors_for_one) / (
         (self.population[0] * transition_factors_for_one) + (
          self.population[1] * transition_factors_for_two))
        fitness_of_two = (self.population[1] * transition_factors_for_two) / (
         (self.population[0] * transition_factors_for_one) + (
           self.population[1] * transition_factors_for_two))
        return fitness_of_one, fitness_of_two

    def __reproduce(self):
        p_a, p_b = self.__compute_fitness()
        # we recalculate the probabilities now with mutation.
        p_a_with_mutation = (1.0-self.mutation_probability)*p_a + self.mutation_probability*(1.0-p_a)
        p_b_with_mutation = (1.0-self.mutation_probability)*p_b + self.mutation_probability*(1.0-p_b)
        to_add = np.random.choice(range(self.number_of_strategies), p=(p_a_with_mutation, p_b_with_mutation))
        self.population[to_add] +=1

    def __to_die_and_replace(self):
        num_to_die = np.random.randint(0, self.number_of_strategies)  # generates a random number with equal probability
        self.population[num_to_die] -= 1

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
        self.__reproduce()
        print("Individual reproduced based upon the fitness function")
        print(self.population)
        print("\n")

        # replace, maybe mutation


def main():
    test = MoranProcess(a=2, b=1, c=2, d=3, w=4, mutation_probability=0.01, population_array= [5, 7])
    for i in range(1, 10):
        test.step()


if __name__ == "__main__":
    main()