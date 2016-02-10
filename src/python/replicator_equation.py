import network as network
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


class ReplicatorDynamics:

    def __init__(self, graph, number_of_players, population_fraction, t_0):
        self.network_game = network.Network(graph, number_of_players)
        self.population_fraction = population_fraction
        self.replicator_trajectory(population_fraction, t_0)

    @staticmethod
    def multinomial_distribution(population_fractions, group_composition):
        a = math.factorial(np.sum(group_composition))
        b = np.prod(np.power(population_fractions, group_composition))
        c = np.product(list((map(math.factorial, group_composition))))
        return a*b/c

    def compute_payoff(self):
        payoff = np.zeros_like(self.network_game.strategy_set)
        for i in self.network_game.payoff:
            payoff += self.multinomial_distribution(self.population_fraction, i) * self.network_game.payoff[i]
        return payoff

    @staticmethod
    def replicator_equation(x, t, payoff):
        fitness_vector = np.dot(payoff, x)
        average_fitness = np.dot(x, fitness_vector)
        return x * (fitness_vector - average_fitness)

    def replicator_trajectory(self, y_0, t_vector):
        soln = odeint(self.replicator_equation, y_0 , t_vector, args=(self.population_fraction,))
        orbits = [soln[:, i] for i in range(len(self.population_fraction))]

        #plotting function here
        #Plotting stuff
        plt.rc('lines', linewidth=2.0)
        plt.figure(figsize=(20,4))
        color=iter(cm.rainbow(np.linspace(0,1,len(orbits))))
        for i in range(len(orbits)):
            c=next(color)
            plt.plot(orbits[i], c=c, label=self.network_game.strategy_names[i])
        plt.rc('lines', linewidth=2.0)
        plt.legend()










