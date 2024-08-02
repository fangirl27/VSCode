class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier(): #lifo
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        #print(type(node))

#if node state is equal to given state for all elements in frontier list, then returns True or Falsey
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

#checks if frontier length is zero
    def empty(self):
        return len(self.frontier) == 0


    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] #-1 means last element. so node stores last element of the array frontier
            self.frontier = self.frontier[:-1] #removes last element from the array
            return node


class QueueFrontier(StackFrontier): #fifo

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
