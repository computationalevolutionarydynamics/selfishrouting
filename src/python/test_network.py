import unittest
import network as network
import networkx as nx
import numpy as np


class TestNetwork(unittest.TestCase):

    def test_braess_network(self):
        my_graph = network.create_braess_network()
        my_network_game = network.Network(my_graph, 2)
        #print(my_network_game.payoff)
        #print(my_network_game.strategy_set)
        profile = (0, 0)
        payoff_expected = np.array([4,4])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (0, 1)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (0, 2)
        payoff_expected = np.array([2,2])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (0, 3)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (1, 0)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (1, 1)
        payoff_expected = np.array([4,4])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (1, 2)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (1, 3)
        payoff_expected = np.array([2,2])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (2, 0)
        payoff_expected = np.array([2,2])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (2, 1)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (2, 2)
        payoff_expected = np.array([4,4])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))



        profile = (2, 3)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))



        profile = (3, 0)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))



        profile = (3, 1)
        payoff_expected = np.array([2,2])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (3, 2)
        payoff_expected = np.array([3,3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (3, 3)
        payoff_expected = np.array([4,4])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        #nx.draw(self.graph)
        #plt.show()
