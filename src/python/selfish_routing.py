import numpy as np
import pandas as pd


class MoranProcess:
    def __init__(self, game_matrix, w, mutation_probability,
                 population_array, time_step):  # removed initial_population add intensity of selection

        """
        This function initialises different instance variables.
        :param game_matrix: ?????
        :param w: intensity of selection
        :param mutation_probability: mutation probability
        :param population_array: put some description here....
        :param time_step: ??
        :return:
        """
        # temporarily we only accept populations of two types

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

        assert time_step >= 1, "Time Step should be greater or equal to 1"
        self.time_step = time_step
        self.time_index = 0

        self.array_of_population = [list(self.population)]
        self.array_of_time_steps = [0]

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
        reproduction_probabilities = np.array(self.__compute_fitness())
        reproduction_probabilities -= (
                                          2 * reproduction_probabilities - 1) * self.mutation_probability
        reproduce = np.random.choice(range(self.number_of_strategies), p=reproduction_probabilities)
        self.population[reproduce] += 1

    def __to_die_and_replace(self):
        num_to_die = np.random.randint(0, self.number_of_strategies)  # generates a random number with equal probability
        self.population[num_to_die] -= 1

    def step(self):

        # select randomly an individual to die
        self.__to_die_and_replace()

        # select randomly an individual to reproduce (fitness proportional)
        self.__reproduce()

        #print(self.population)
        self.time_index += 1
        if self.time_index == self.time_step:
            # put the polpulation in array after the time steps specified by time_step parameter
            self.array_of_population.append(list(self.population))
            self.array_of_time_steps.append(self.array_of_time_steps[len(self.array_of_time_steps)-1] + self.time_step)
            self.time_index=0

    def print_table_and_save_to_file(self):
        # prepare data
        table = pd.DataFrame(data=list(zip(self.array_of_time_steps,self.array_of_population)), columns=['TimeStep',['A', 'B']]) #should be more than A B can be any number
        table.reset_index(level="TimeStep", inplace=True)
        print(table)
        #table.to_csv('data.csv',index=False,header=False)


def main():
    test = MoranProcess([[3, 0], [4, 1]], w=5, mutation_probability=0.001, population_array=[60, 40], time_step=10)

    for i in range(1, 100):
        test.step()

    test.print_table_and_save_to_file()


if __name__ == "__main__":
    main()
