from Node import *


class Edge:

    def __init__(self, node_i, node_j, initial_value):
        # Note the original formulation that w_{i,j} = w_{j,i}
        self.node_i = node_i
        self.node_j = node_j
        self.weight = initial_value

    def change_weight(self, new_value):
        self.weight = new_value

    def get_other_node(self, node):
        node_index = node.index
        if node_index == self.node_i.index:
            return self.node_j
        elif node_index == self.node_j.index:
            return self.node_i
        else:
            return None

    def get_nodes(self):
        return [self.node_i, self.node_j]
