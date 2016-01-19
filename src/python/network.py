import networkx as nx
import matplotlib.pyplot as plt
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

    def traffic_edge(self, node1, node2, profile = []):
        print(profile)
        print(node1)
        print(node2)
        print(self.graph.get_edge_data(node1, node2).get("object")(2))


def create_braess_network():
        my_graph = nx.Graph()
        my_graph.add_edge("S", "A", object=Network.linear)
        my_graph.add_edge("S", "B", object=Network.linear)
        my_graph.add_edge("A", "B", object=Network.constant)
        my_graph.add_edge("A", "T", object=Network.linear)
        my_graph.add_edge("B", "T", object=Network.linear)
        return my_graph



