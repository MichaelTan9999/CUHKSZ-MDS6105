# source: https://github.com/abpaudel/8-puzzle
import numpy as np

# zero is the space in puzzle
class Node:
    parent = None
    state = None
    depth = 0
    zero = None
    cost = 0

    def __init__(self, state, parent, depth=0):
        self.parent = parent
        self.state = np.array(state)
        self.depth = depth
        self.zero = self.find_0()


    def __str__(self):
        return str(self.state[:3]) + '\n' \
               + str(self.state[3:6]) + '\n' \
               + str(self.state[6:]) + ' depth = %d\n '%(self.depth)

    def find_0(self):
        for i in range(9):
            if self.state[i] == 0:
                return i

    def swap(self, i, j):
        new_state = np.array(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def up(self):
        if self.zero > 2:
            return Node(self.swap(self.zero, self.zero - 3), self, self.depth + 1)
        else:
            return None

    def down(self):
        if self.zero < 6:
            return Node(self.swap(self.zero, self.zero + 3), self, self.depth + 1)
        else:
            return None

    def left(self):
        if self.zero % 3 != 0:
            return Node(self.swap(self.zero, self.zero - 1), self, self.depth + 1)
        else:
            return None

    def right(self):
        if (self.zero + 1) % 3 != 0:
            return Node(self.swap(self.zero, self.zero + 1), self, self.depth + 1)
        else:
            return None

    def neighbors(self):
        neighbors = [self.up(), self.down(), self.left(), self.right()]
        return list(filter(None, neighbors))

    def equals(self, node):
        if tuple(self.state) == tuple(node.state):
            return True
        return False

    __repr__ = __str__
