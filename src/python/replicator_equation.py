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


def replicator_equation(x, t, number_of_players):
    G = network.create_braess_network()
    t = ReplicatorDynamics(G, number_of_players)
    fitness_vector = t.compute_payoff(x)
    average_fitness = np.dot(x, fitness_vector)
    return x * (fitness_vector - average_fitness)












