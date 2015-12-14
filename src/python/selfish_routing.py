import numpy as np


class MoranProcess:
    def __init__(self, game_matrix, w, mutation_probability,
                 population_array):  # removed initial_population add intensity of selection

        """
        This function initialises different instance variables.
        :param number_of_strategies:
        :param game_matrix: ?????
        :param w: intensity of selection
        :param mutation_probability: mutation probability
        :param population_array: put some description here....
        :return:
        """
        # temporarily we only accept populations of two types
        assert game_matrix.shape[0] == game_matrix.shape[1], "Matrix should be square"
        self.game_matrix = game_matrix
        self.number_of_strategies = game_matrix.shape[0]
        assert len(
            population_array) == self.number_of_strategies, "Number of strategies does not agree with population array"
        self.population = np.array(population_array, dtype=int)
        self.population_size = np.sum(self.population)
        assert self.population_size >= 2, "Population should be larger than 1"
        assert w >= 0, "Intensity of selection should be 0 or positive"
        self.w = w
        assert 0 <= mutation_probability <= 1, "Mutation probability should be in [0, 1]"
        self.mutation_probability = mutation_probability

    def __compute_payoff(self):
        """
        We need some more detailed comments here... maybe...
        :return:
        """
        return (np.dot(self.game_matrix, self.population) - np.diag(self.game_matrix)) / (self.population_size - 1)

    def __compute_fitness(self):
        # calculate transition from payoff to fitness
        payoff_vector = self.__compute_payoff()
        probabilities = self.population * np.exp(self.w * payoff_vector)
        return probabilities / np.sum(probabilities)

    def __reproduce(self):
        # we recalculate the probabilities now with mutation.
        v = np.array([self.__compute_fitness()])
        v1 = v
        v = self.mutation_probability * ((2 * v) - 1)
        v = v1 - v
        to_add = np.random.choice(range(self.number_of_strategies), p=v)
        self.population[to_add] += 1

    def __to_die_and_replace(self):
        num_to_die = np.random.randint(0, self.number_of_strategies)  # generates a random number with equal probability
        self.population[num_to_die] -= 1

    def step(self):
        # generate population
        print("Initial population")
        print(self.population)

        # select randomly an individual to die
        print("Individual selected and died")
        self.__to_die_and_replace()
        print("Population after the death")
        print(self.population)

        # select randomly an individual to reproduce (fitness proportional)
        self.__reproduce()
        print("Individual reproduced based upon the fitness function")
        print(self.population)
        print("\n")


def main():
    test = MoranProcess(game_matrix=[[1, 2], [3, 4]], w=5, mutation_probability=0.01, population_array=[5, 7])
    for i in range(1, 10):
        test.step()


if __name__ == "__main__":
    main()
