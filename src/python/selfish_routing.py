
import numpy as np


class MoranProcess:

    def __init__(self, number_of_strategies, population_size, a, b, c, d, w):  # removed initial_population add intensity of selection

        assert population_size >= 2 , "Population should be larger than 1"
        self.number_of_strategies = number_of_strategies
        self.population_size = population_size
        self.population = np.array([])
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.w = w

    def __generate_population(self): # generates a random population

        i = 0

        while i < self.population_size:
            gen_ran_num = np.random.randint(1, self.number_of_strategies + 1, 1)  # generates a random number with equal probablity
            self.population = np.append(self.population, gen_ran_num)
            i += 1

    def __compute_payoff(self):
        # calculate number of differnt types in population
        sum_of_ones = 0
        sum_of_tows = 0
        for i in range(len(self.population)):
            if self.population[i] == 1:
                sum_of_ones += 1
            else:
                sum_of_tows += 1

        #print(sum_of_ones)
        #print(sum_of_tows)

        temp_a1 = ((sum_of_ones - 1 ) * self.a) / (self.population_size - 1)
        temp_a2 = ((sum_of_tows ) * self.b) / (self.population_size - 1)
        payoff_of_a = temp_a1 + temp_a2
        #print(payoff_of_a)

        temp_b1 = ((sum_of_ones) * self.c) / (self.population_size - 1)
        temp_b2 = ((sum_of_tows - 1) * self.d ) / (self.population_size - 1)
        payoff_of_b = temp_b1 + temp_b2
        #print(payoff_of_b)

        l1 = [payoff_of_a, payoff_of_b]
        return l1


    def __compute_fitness (self):
        return

    def __to_reproduce (self):
        return

    def __to_die_and_replace (self):
        num_to_die = np.random.randint(1, self.number_of_strategies + 1, 1)  # generates a random number with equal probablity
        self.population = np.delete(self.population, num_to_die)

    def __mutate (self):
        return

    def __replace (self):
        return

    def step(self):

        #generate population
        self.__generate_population()
        print("Initial population \n")
        print (self.population)

        #compute payoffs
        var = self.__compute_payoff
        print("The payoffs are \n")
        print(var)

        # compute fitness

        # select randomly an individual to reproduce (fitness proportional)

        # select randomly an individual to die
        print("Individual selected and died \n")
        self.__to_die_and_replace()
        print("Population after the death\n")
        print (self.population)

        # replace, maybe mutation

test = MoranProcess(2,10,1,2,3,4,5)
test.step()







