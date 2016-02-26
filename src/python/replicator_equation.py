import network as network
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


class ReplicatorDynamics:
    def __init__(self, graph, number_of_players):
        """
        :param graph: graph created using network class
        :param number_of_players: number of players in the game
        :return:
        """
        self.network_game = network.Network(graph, number_of_players)
        self.number_of_players = number_of_players

    @staticmethod
    def multinomial_distribution(population_fractions, group_composition):
        """"
        calculates the probablity using the multinomial distribution formulae

        :param population_fractions: an array indicating various population fractions in population
        :param group_composition: an array indicationg which player is playing which strategy in the group
        """
        a = math.factorial(np.sum(group_composition))
        b = np.prod(np.power(population_fractions, group_composition))
        c = np.product(list((map(math.factorial, group_composition))))
        return a*b/c

    @staticmethod
    def create_mutation_matrix(u, number_of_strategies):
        """
        creates an NxN mutation matrix whose every row adds up to one
        
        :param u: mutation probablity
        :param number_of_strategies: number of strategies in the game
        :return: an NxN mutation matrix
        """
        mutation_matrix = np.ones(shape=(number_of_strategies, number_of_strategies))
        for i in range(len(mutation_matrix)):
            for j in range(len(mutation_matrix)):
                if i == j:
                    mutation_matrix[i,j] = 1-(number_of_strategies - 1)*u
                else:
                    mutation_matrix[i,j] = u

        return np.array(mutation_matrix, dtype=float)

    def compute_payoff(self, population_fraction):
        """
        calculates payoff for each strategy using the multinomial distribution method
        :param population_fraction:
        :return: an array indicating payoffs
        """
        payoff = np.zeros_like(self.network_game.strategy_set)
        for i in self.network_game.payoff:
            payoff += self.multinomial_distribution(population_fraction, i) * self.network_game.payoff[i]
        return -1.0 * np.array(payoff, dtype=float)

    def replicator_trajectory(self, t_vector, population_fraction, **kwargs):
        soln = odeint(replicator_equation, population_fraction, t_vector, args=(self.number_of_players,))
        orbits = [soln[:, i] for i in range(len(population_fraction))]

        #Plotting stuff
        plt.rc('lines', linewidth=2.0)
        plt.figure(figsize=(20,4))
        color=iter(cm.rainbow(np.linspace(0,1,len(orbits))))
        for i in range(len(orbits)):
            c=next(color)
            plt.plot(t_vector, orbits[i], c=c, label=self.network_game.strategy_names[i])
        plt.rc('lines', linewidth=2.0)
        plt.legend()

        for i in range(len(orbits)):
            print(orbits[i][-1])

    def replicator_mutator_trajectory(self, t_vector, population_fraction, u,  **kwargs):
        mutation_matrix = self.create_mutation_matrix(u, len(self.network_game.strategy_set))
        soln= odeint(replicator_mutator_equation, population_fraction, t_vector, args=(self.number_of_players, mutation_matrix, ))
        orbits = [soln[:, i] for i in range(len(population_fraction))]

        #Plotting stuff
        plt.rc('lines', linewidth=2.0)
        plt.figure(figsize=(20,4))
        color=iter(cm.rainbow(np.linspace(0,1,len(orbits))))
        for i in range(len(orbits)):
            c=next(color)
            plt.plot(t_vector, orbits[i], c=c, label=self.network_game.strategy_names[i])
        plt.rc('lines', linewidth=2.0)
        plt.legend()

        for i in range(len(orbits)):
            print(orbits[i][-1])


def replicator_equation(x, t, number_of_players):
    x /= np.sum(x)
    G = network.create_braess_network()
    R = ReplicatorDynamics(G, number_of_players)
    fitness_vector = R.compute_payoff(x)
    average_fitness = np.dot(x, fitness_vector)
    return x * (fitness_vector - average_fitness)


def replicator_mutator_equation(x, t, number_of_players, mutation_matrix):
    x /= np.sum(x)
    G = network.create_braess_network()
    R = ReplicatorDynamics(G, number_of_players)
    fitness_vector = R.compute_payoff(x)
    average_fitness = np.dot(x, fitness_vector)

    temp = np.zeros_like(R.network_game.strategy_set)

    for i in range(len(R.network_game.strategy_set)):
        for j in range(len(R.network_game.strategy_set)):
            temp[i] += (x[j] * fitness_vector[j] * mutation_matrix[j,i]) #- (x[i] * average_fitness)

    b = x * average_fitness
    c = np.array(temp) - b
    return np.array(c, dtype=float)


#G = network.create_braess_network()
#t_vector = np.linspace(0, 10, 10000)
#pop = [0.1, 0.4, 0.2, 0.3]
#t = ReplicatorDynamics(G, 5)
#t.replicator_mutator_trajectory(t_vector, pop , u = 0.0005, maximum_iterations= 10000)
#t.replicator_trajectory(t_vector, pop ,maximum_iterations= 95000)







