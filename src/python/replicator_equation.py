import network as network
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


class ReplicatorDynamics:
    def __init__(self, graph, number_of_players):
        self.network_game = network.Network(graph, number_of_players)
        self.number_of_players = number_of_players

    @staticmethod
    def multinomial_distribution(population_fractions, group_composition):
        a = math.factorial(np.sum(group_composition))
        b = np.prod(np.power(population_fractions, group_composition))
        c = np.product(list((map(math.factorial, group_composition))))
        return a*b/c

    def compute_payoff(self, population_fraction):
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
            plt.plot(orbits[i], c=c, label=self.network_game.strategy_names[i])
        plt.rc('lines', linewidth=2.0)
        plt.legend()

    def replicator_mutator_trajectory(self, t_vector, population_fraction, u,  **kwargs):
        mutation_matrix = self.create_mutation_matrix(u, len(self.network_game.strategy_set))
        soln = odeint(replicator_mutator_equation, population_fraction, t_vector, args=(self.number_of_players, mutation_matrix, ))

        orbits = [soln[:, i] for i in range(len(population_fraction))]

        #Plotting stuff
        plt.rc('lines', linewidth=2.0)
        plt.figure(figsize=(20,4))
        color=iter(cm.rainbow(np.linspace(0,1,len(orbits))))
        for i in range(len(orbits)):
            c=next(color)
            plt.plot(orbits[i], c=c, label=self.network_game.strategy_names[i])
        plt.rc('lines', linewidth=2.0)
        plt.legend()

    def create_mutation_matrix(self, u, number_of_strategies):
        mutation_matrix = np.ones(shape = (number_of_strategies, number_of_strategies))
        for i in range(len(mutation_matrix)):
            for j in range(len(mutation_matrix)):
                if i == j:
                    mutation_matrix[i,j] = 1-2*u
                else:
                    mutation_matrix[i,j] = u

        return mutation_matrix


def replicator_equation(x, t, number_of_players):
    G = network.create_braess_network()
    t = ReplicatorDynamics(G, number_of_players)
    fitness_vector = t.compute_payoff(x)
    average_fitness = np.dot(x, fitness_vector)
    return x * (fitness_vector - average_fitness)


def replicator_mutator_equation(x, t, number_of_players, mutation_matrix):
    G = network.create_braess_network()
    t = ReplicatorDynamics(G, number_of_players)
    fitness_vector = t.compute_payoff(x)
    average_fitness = np.dot(x, fitness_vector)
    # dispell the sum here, so that mutation matrix can be included
    a = np.dot(x * fitness_vector, mutation_matrix)
    b = x * average_fitness
    return a - b












