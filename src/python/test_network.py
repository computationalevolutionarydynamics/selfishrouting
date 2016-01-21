import unittest
import network as network
import networkx as nx
import numpy as np


class TestNetwork(unittest.TestCase):

    def test_profile_generation(self):
        my_simple_graph = network.create_simple_network()
        my_network_simple_game = network.Network(my_simple_graph, 3)

        profile_expected = (0,3)
        computed_profile =  my_network_simple_game.profiles[0]
        self.assertEqual(profile_expected,computed_profile, msg="test failed")

        profile_expected = (1,2)
        computed_profile =  my_network_simple_game.profiles[1]
        self.assertEqual(profile_expected,computed_profile, msg="test failed")

        profile_expected = (2,1)
        computed_profile =  my_network_simple_game.profiles[2]
        self.assertEqual(profile_expected,computed_profile, msg="test failed")

        profile_expected = (3,0)
        computed_profile =  my_network_simple_game.profiles[3]
        self.assertEqual(profile_expected,computed_profile, msg="test failed")



    def test_braess_network(self):
        my_graph = network.create_braess_network()
        my_network_game = network.Network(my_graph, 2)
        #print(my_network_game.payoff)
        #print(my_network_game.strategy_set)
        profile = (0, 0, 0, 2)
        payoff_expected = np.array([0, 0, 0, 4])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (0, 0, 1, 1)
        payoff_expected = np.array([0, 0, 3, 3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (0, 0, 2, 0)
        payoff_expected = np.array([0, 0, 4, 0])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (0, 1, 0, 1)
        payoff_expected = np.array([0, 2, 0, 2])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (0, 1, 1, 0)
        payoff_expected = np.array([0, 3, 3, 0])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (0, 2, 0, 0)
        payoff_expected = np.array([0, 4, 0, 0])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (1, 0, 0, 1)
        payoff_expected = np.array([3, 0, 0, 3])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        profile = (1, 0, 1, 0)
        payoff_expected = np.array([2, 0, 2, 0])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (1, 1, 0, 0)
        payoff_expected = np.array([3, 3, 0, 0])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))


        profile = (2, 0, 0, 0)
        payoff_expected = np.array([4, 0, 0, 0])
        computed_payoff =  my_network_game.payoff[profile]
        np.testing.assert_almost_equal(payoff_expected, computed_payoff, decimal=3, err_msg=
                                       "Payoff for profile {} should be {}, but it is {}".format(profile, payoff_expected, computed_payoff))

        #nx.draw(self.graph)
        #plt.show()

