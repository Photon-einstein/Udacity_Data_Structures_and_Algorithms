# For this exercise we will be using an Adjacency List representation to store the graph.

# Class Node representation.
class Node:
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self, new_node):
        self.children.append(new_node)
    
    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph():
    def __init__(self, node_list):
        self.nodes = node_list
        
    def add_edge(self, node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

# Creating a graph as above.
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 

graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph1.nodes:
    print('parent node = ',each.value,end='\nchildren\n')
    for each in each.children:
        print(each.value,end=' ')
    print('\n')

'''TO DO'''
def dfs_recursion_start(start_node, search_value):
    if start_node.value == search_value:
        return start_node
    visited = [start_node]
    for child in start_node.children:
        return dfs_recursion(child, search_value, visited)
    return None

def dfs_recursion(start_node, search_value, visited):
    if start_node.value == search_value:
        return start_node
    visited.append(start_node)
    for child in start_node.children:
        if child not in visited:
            result =  dfs_recursion(child, search_value, visited)
            if result is not None:
                return result
    return None

assert nodeA == dfs_recursion_start(nodeG, 'A')
assert nodeA == dfs_recursion_start(nodeS, 'A')
assert nodeS == dfs_recursion_start(nodeP, 'S')
assert nodeR == dfs_recursion_start(nodeH, 'R')
