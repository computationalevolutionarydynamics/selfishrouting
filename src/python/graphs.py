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
        self.G.add_edge("S", "B", object=self.linear)
        self.G.add_edge("A", "B", object=self.constant)
        self.G.add_edge("A", "T", object=self.linear)
        self.G.add_edge("B", "T", object=self.linear)
        #nx.draw(self.G)
        #plt.show()

    def __enumerate_strategies_and_payoffs(self, number_of_players):
        for i in nx.all_simple_paths(self.G, "S", "T"):
            self.strategy_set.append(i)
        list_of_strategies = list(self.strategy_set)
        print(list_of_strategies)

        temp_string = ""
        for i in range(0,len(list_of_strategies)):
            temp_string += str(i)

        player_options = [''.join(i) for i in it.product(temp_string, repeat=number_of_players)]
        print(player_options)

        for i in player_options:
            for j in range(0,len(i)):
                for k in range(0,len(list_of_strategies[int(i[j])])-1):
                    #print(list_of_strategies[int(i[j])][k])
                    #print(list_of_strategies[int(i[j])][k+1])
                    self.traffic_edge(list_of_strategies[int(i[j])][k], list_of_strategies[int(i[j])][k+1], i)
            break




    def traffic_edge(self, node1, node2, profile = []):
        print(profile)
        print(node1)
        print(node2)


    def test_func(self):
        self.__create_graph()
        self.__enumerate_strategies_and_payoffs(2)

t1 = test()
t1.test_func()


