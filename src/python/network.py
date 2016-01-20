import networkx as nx
import itertools as it


class Network:

    def __init__(self, graph, number_of_players):
        self.graph = graph
        assert "S" in graph.nodes(), "Graph needs to have a node labeled S"
        assert "T" in graph.nodes(), "Graph needs to have a node labeled T"
        # First enumerate all strategies available from the given graph
        self.strategy_set = []
        for i in nx.all_simple_paths(self.graph, "S", "T"):
            self.strategy_set.append(i)

        # Then, create all possible profiles corresponding to the set of strategies
        enumeration = []
        for i, strategy in enumerate(self.strategy_set):
            enumeration.append(i)
        self.profiles = list(it.product(enumeration, repeat=number_of_players))

        # Then create the payoff function, which is a dictionary
        # where keys are profiles (tuples of int), and values
        # are payoffs

        payoff = []
        self.profiles_with_payoffs = {}
        for i in self.profiles:
            for j in range(0,len(i)):
                payoff.append(self.traffic_edge(self.graph, self.strategy_set[int(i[j])], i, j))
            self.profiles_with_payoffs[i] = payoff[:]
            payoff.clear()

        print(self.profiles)
        print(self.strategy_set)
        print(self.profiles_with_payoffs)
   # Latency functions

    @staticmethod
    def linear(x):
        return x

    @staticmethod
    def constant(x):
        return 0

    @staticmethod
    def quadratic(x):
        return x**2.0

    # End of latency functions

    def traffic_edge(self, graph, strategy, profile, position):

        traffic = 0
        payoff = 0
        for i in range(0, len(strategy)-1):
            traffic += 1
            for j in range(0, len(profile)): # position of the index j in profile is the index whose traffic is to be determined
                if j == position:
                    pass
                elif profile[position] == profile[j]: #both have same profile
                    traffic += 1
                else:
                    if self.search_for_edges(strategy[i], strategy[i+1], strategy):
                        traffic += 1
            payoff += self.graph.get_edge_data(strategy[i], strategy[i+1]).get("object")(traffic)

        return payoff

    def search_for_edges(self, node1, node2, strategy):
        #print(strategy)
        #print(node1)
        #print(node2)
        if node1 in strategy:
            if node2 == strategy[strategy.index(node1) + 1]:
                return True
        return False



def create_braess_network():
        my_graph = nx.Graph()
        my_graph.add_edge("S", "A", object=Network.linear)
        my_graph.add_edge("S", "B", object=Network.linear)
        my_graph.add_edge("A", "B", object=Network.constant)
        my_graph.add_edge("A", "T", object=Network.linear)
        my_graph.add_edge("B", "T", object=Network.linear)
        return my_graph



t1 = Network(create_braess_network(), 2)