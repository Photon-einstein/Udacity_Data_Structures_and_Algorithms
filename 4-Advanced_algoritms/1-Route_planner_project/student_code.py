import heapq
import math

class Node:
    def __init__(self, index):
        self.parent = -1  # To signal not initiated
        self.index = index
        self.f = float('inf')  # f = g + h
        self.g = float('inf')  # Cost from start to this node
        self.h = float('inf')  # Heuristic from this node to destination

def shortest_path(M, start, goal):
    if start not in M.intersections or goal not in M.intersections:
        print("Start node or goal node not in the map.")
        return []
    elif start == goal:
        print("Start and goal are the same, no work to do")
        return [start]

    numberNodeGraph = len(M.intersections)
    closedList = set()  # Using a set for fast lookup
    nodeData = [Node(i) for i in range(numberNodeGraph)]
    openList = []
    openSet = {}  # Dictionary to track open list nodes
    
    # Initialize start node
    nodeData[start].parent = start
    nodeData[start].g = 0
    nodeData[start].h = heuristic_calc(M, start, goal)
    nodeData[start].f = nodeData[start].g + nodeData[start].h
    
    heapq.heappush(openList, (nodeData[start].f, nodeData[start]))
    openSet[start] = nodeData[start]

    while openList:
        # Get node with lowest f value
        _, current_node = heapq.heappop(openList)
        del openSet[current_node.index]

        # If goal is reached, reconstruct path
        if current_node.index == goal:
            return reconstruct_path(nodeData, start, goal)

        closedList.add(current_node.index)

        for neighbour in M.roads[current_node.index]:
            if neighbour in closedList:
                continue  # Skip already visited nodes

            g_new = current_node.g + g_path_calc(M, current_node.index, neighbour)
            h_new = heuristic_calc(M, neighbour, goal)
            f_new = g_new + h_new

            if neighbour in openSet:
                # If new f is better, update node data
                if f_new < nodeData[neighbour].f:
                    nodeData[neighbour].parent = current_node.index
                    nodeData[neighbour].g = g_new
                    nodeData[neighbour].f = f_new
                    heapq.heappush(openList, (f_new, nodeData[neighbour]))
                    openSet[neighbour] = nodeData[neighbour]
            else:
                # New node, add to open list
                nodeData[neighbour].parent = current_node.index
                nodeData[neighbour].g = g_new
                nodeData[neighbour].f = f_new
                heapq.heappush(openList, (f_new, nodeData[neighbour]))
                openSet[neighbour] = nodeData[neighbour]

    print("No path found.")
    return []

def heuristic_calc(M, start, goal):
    """Compute heuristic as Euclidean distance"""
    return math.sqrt((M.intersections[start][0] - M.intersections[goal][0]) ** 2 +
                     (M.intersections[start][1] - M.intersections[goal][1]) ** 2)

def g_path_calc(M, start, goal):
    """Compute path cost as Euclidean distance"""
    return math.sqrt((M.intersections[start][0] - M.intersections[goal][0]) ** 2 +
                     (M.intersections[start][1] - M.intersections[goal][1]) ** 2)


def reconstruct_path(nodeData, start, goal):
    path = []
    current = goal
    while (current != start):
        path.append(current)
        current = nodeData[current].parent
    path.append(start)
    path.reverse()
    return path
