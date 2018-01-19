from random import randint

class Node:
    def __init__(self, idx=0, x=0, y=0, z=0):
        self.idx = idx
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "%d, %d, %d\n" % (self.x, self.y, self.z)

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __str__(self):
        return "%d, %d\n" % (self.node1.idx, self.node2.idx)

class RoadNetwork:
    def __init__(self):
        node_first = Node(0, 1, 1, 1)
        node_second = Node(1, 2, 2, 2)
        self.nodes = [node_first, node_second]
        self.edges = [Edge(node_first, node_second)]

    def add_edge(self):
        start_node = self.nodes[randint(0, len(self.nodes)-1)]
        end_node = Node(len(self.nodes), randint(1,20), randint(1,20), randint(1,20))
        self.nodes.append(end_node)
        self.edges.append(Edge(start_node, end_node))
    
    def __str__(self):
        ret_string = ''
        for node in self.nodes:
            ret_string += str(node)
    
        for edge in self.edges:
            ret_string += str(edge)
        
        return ret_string

if __name__ == '__main__':
    road_network = RoadNetwork()
    
    for n in range(10):
        road_network.add_edge()

    print road_network
