import numpy as np
import pandas as pd
import string


class MoranProcess:
    def __init__(self, game_matrix, w, mutation_probability,
                 population_array, seed = None):  # removed initial_population add intensity of selection

        """
        This function initialises different instance variables.
        :param game_matrix: ?????
        :param w: intensity of selection
        :param mutation_probability: mutation probability
        :param population_array: put some description here....
        :param seed: put some description here....
        :return:
        """
        # temporarily we only accept populations of two types
        if seed is not None:
            np.random.seed(seed)
        self.game_matrix = np.array(game_matrix)
        assert self.game_matrix.shape[0] == self.game_matrix.shape[1], "Matrix should be square"

        self.number_of_strategies = self.game_matrix.shape[0]
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

    def step(self):
        try:
            # we recalculate the probabilities now with mutation.
            reproduction_probabilities = np.array(self.__compute_fitness())
            reproduction_probabilities -= (
                                          2.0 * reproduction_probabilities - 1.0) * self.mutation_probability
            reproduction_probabilities = reproduction_probabilities/ np.sum(reproduction_probabilities)
            reproduce = np.random.choice(range(self.number_of_strategies), p=reproduction_probabilities)
            die = np.random.choice(range(self.number_of_strategies), p=self.population/self.population_size)
            self.population[reproduce] += 1
            self.population[die] -= 1
        except ValueError:
            raise Exception("Exception with probabilities {}".format(reproduction_probabilities))

    def run_time_series(self, number_of_steps, print_every_time_steps=1):
        assert print_every_time_steps >= 1, "Time Step should be greater or equal to 1"
        assert number_of_steps >=1, "Number of steps needs to be larger than 0"
        array_of_population = [list(self.population)]
        array_of_time_steps = [0]
        for time_step in range(1, number_of_steps+1):
            self.step()
            if time_step%print_every_time_steps == 0:
                array_of_population.append(list(self.population))
                array_of_time_steps.append(time_step)
        column_array = list(map(chr, range(97, 97+len(self.population))))
        df = pd.DataFrame(data=array_of_population, columns=column_array, index=array_of_time_steps)
        df.index.names = ['Time Steps']
        return df

def main():
     test = MoranProcess([[3, 0, 1, 2], [4, 1, 1, 7], [2, 5, 1, 9], [2, 3, 1, 2]], w=5, mutation_probability=0.001, population_array=[60, 30, 5, 5], seed = 123)
     df = test.run_time_series(1000, 10)
     df.to_csv("my_simulation.csv")
     print(df.head())


if __name__ == "__main__":
     main()