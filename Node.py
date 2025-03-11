class Node:

    def __init__(self, node_index):
        self.value = -1
        self.index = node_index

    def change_value(self, new_value):
        if new_value not in [-1, 1]:
            raise Exception("Neuron Values are either -1 or 1")

        self.value = new_value
