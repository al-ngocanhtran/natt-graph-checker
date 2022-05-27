from collections import defaultdict
import time
import networkx as nx
import matplotlib.pyplot as plt

# defaultdict stores Dict but different from Dict as it does not
# raise KeyError but returns default value for non-existing key

'''
    Input: Receive a nested list of edges from users/ file analysed
    Output: Yes/No Answer
'''


class Graph:

    ''' 
    Check Eulerian graph: connected and each vertice has even edges
    listE = [[v1, v4], [v2, v3]] e.g
    '''

    def __init__(self, listE, listV):
        self.listE = listE  # no of vertices
        self.graph = defaultdict(list)
        self.createEdge()
        self.listV = listV

    # Creating a graph with the given vertices
    def createEdge(self):
        for elm in self.listE:
            if len(elm) == 2:
                v1 = elm[0]
                v2 = elm[1]
                if v1 != v2:
                    self.graph[v1].append(v2)
                    self.graph[v2].append(v1)

    # Check visited vertices by DFS to check if graph is connected
    def DFSearch(self, v, visited):
        # Mark the current node as visited
        visited[v] = True

        # Recur to check all the adjacent vertices to the current vertice
        print('self Graph: ', self.graph)
        neighbors = self.graph[v]
        for i in neighbors:
            if visited[i] == False:
                print('check visited v', i)
                self.DFSearch(i, visited)

    # Check if graph is connected
    def isConnected(self):
        # initializing a list of vertices with none visited
        size = len(self.graph)
        visited = [False]*(size)
        print('Visited: ', visited)

        # DFS should start visitedV
        visitedV = 0
        # Find a vertex with non-zero degree to start the algorithm
        for index, key in enumerate(self.graph):
            if len(self.graph[key]) > 1:
                visitedV = index
                break
            # If there are no edges in the graph, return true
            if index == size - 1:
                return True

        self.DFSearch(visitedV, visited)

        # Check if all non-zero degree vertices are visited
        for j in range(size):
            if visited[j] == False and len(self.graph[j]) > 0:
                return False
        return True

    def isEulerian(self):
        # Check if all non-zero degree vertices are connected
        if self.isConnected() == False:
            return 0
        else:
            # Meet condition: Graph is connected
            odd = 0
            for i in range(len(self.graph)):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
            '''
            Scenario: 
            - odd = 2 => Graph is semi-eulerian 
            - odd = 0 => Graph is eulerian 
            - odd > 2 => Graph is not eulerian 
            '''
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0

    def test(self):
        res = self.isEulerian()
        if res == 0:
            # Check Planar here
            return "Graph is not Eulerian graph"
        elif res == 1:
            return "Graph is a Semi-eulerian graph (having a Euler path)"
        else:
            return "Graph is a Eulerian graph (having a Euler cycle)"


class Visualization:

    def drawGraph(G, graph, result):
        for pair in graph.listE:
            v1 = str(pair[0])
            v2 = str(pair[1])
            if v1 in graph.listV:
                graph.listV.remove(v1)
            if v2 in graph.listV:
                graph.listV.remove(v2)
            G.add_edge(pair[0], pair[1])
        for v in graph.listV:
            G.add_node(v)
        plt.figure(figsize=(10, 5))
        ax = plt.gca()
        ax.set_title(result)
        nx.draw(G, with_labels=True, node_color="pink")
        plt.show(block=False)
        plt.pause(5)
        # plt.savefig(filename)
        plt.close()

    def main(listE, listV):
        G = nx.Graph()
        inputGraph = Graph(listE, listV)
        result = inputGraph.test()
        Visualization.drawGraph(G, inputGraph, result)
