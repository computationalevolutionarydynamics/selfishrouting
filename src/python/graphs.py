import networkx as nx
import matplotlib.pyplot as plt
import itertools as it


class test:
    def __init__(self):
        self.G = nx.Graph()
        self.strategy_set = []

    def linear(self, x):
        return x

    def constant(self):
        return 0

    def quadratic(self, x):
        return x**2.0

    def __create_graph(self):
        self.G.add_edge("S", "A", object=self.linear)
        self.G.add_edge("S", "B", object=self.quadratic)
        self.G.add_edge("A", "B", object=self.constant)
        self.G.add_edge("A", "T", object=self.linear)
        self.G.add_edge("B", "T", object=self.linear)
        #nx.draw(self.G)
        #plt.show()

    def __enumerate_strategies_and_payoffs(self, number_of_players):
        for i in nx.all_simple_paths(self.G, "S", "T"):
            self.strategy_set.append(i)
        #temp_list = list(enumerate(self.strategy_set))
        temp_list = list(self.strategy_set)
        print(temp_list)

        temp_string = ""
        for i in range(0,len(temp_list)):
            temp_string += str(i)

        temp = [''.join(i) for i in it.product(temp_string, repeat=number_of_players)]
        print(temp)




    def test_func(self):
        self.__create_graph()
        self.__enumerate_strategies_and_payoffs(2)

t1 = test()
t1.test_func()


