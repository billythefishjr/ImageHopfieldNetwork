from Weight import *
from Node import *
import numpy as np
import random as rand


class Network:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self):
        new_node_index = len(self.nodes)
        new_node = Node(new_node_index)
        self.nodes.append(new_node)

    def create_edges(self):
        for node_i in self.nodes:
            for node_j in self.nodes:
                new_edge = Edge(node_i, node_j, 0)
                if new_edge not in self.edges:
                    self.edges.append(new_edge)

    def find_node(self, index):
        for node in self.nodes:
            if node.index == index:
                return node

        return None

    def set_state(self, state):
        if len(state) != len(self.nodes):
            raise Exception("Cannot Create state of different size than network")

        for i in range(len(state)):
            self.nodes[i].change_value(state[i])

    def inference(self, initial_state_array):
        self.set_state(initial_state_array)

        nodes_to_visit = self.nodes.copy()
        while nodes_to_visit:
            j = rand.randint(0, len(nodes_to_visit) - 1)
            node_j = nodes_to_visit[j]
            weighted_sum = 0
            for edge in self.edges:
                other_node = edge.get_other_node(node_j)
                if other_node:
                    weighted_sum += other_node.value * edge.weight

            actual_node = self.find_node(node_j.index)
            if weighted_sum > 0:
                actual_node.value = 1
            elif weighted_sum < 0:
                actual_node.value = -1
            else:
                raise Exception("Isolated Node")

            nodes_to_visit.remove(node_j)

    def learn(self, state_to_learn):
        self.set_state(state_to_learn)
        for edge in self.edges:
            [node_i, node_j] = edge.get_nodes()
            edge.weight += 2 * node_i.value * node_j.value
