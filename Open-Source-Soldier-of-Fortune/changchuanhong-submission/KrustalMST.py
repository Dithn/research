"""
Submission by: @changchuanhong

This is the main module required to compute the Minimum Spanning Tree.
"""

# Imports
import numpy as np

class MST:
    """
    This module contains all the logic required to compute and return a Minimum Spanning Tree.
    """
    def __init__(self, distance_matrix):
        """
        Constructor

        :param distance_matrix: A NxN matrix of distances
        """
        self.setDistanceMatrix(distance_matrix)

    def DepthFirstSearch(self, current_node, visited):
        """
        Depth First Search Algorithm.

        :param current_node: (int)The current node that we are evaluating to determine all other reachable nodes.
        :param visited:      (list) An array that indicates whether a node has been visited. A value of 1 indicates that the node has been visited.
        """
        # mark as visited
        visited[current_node] = 1
    
        for i in range(self.node_count):
            if self.adjacency_matrix[current_node][i] == 1 and not visited[i]:
                self.DepthFirstSearch(i, visited)
        return visited

    def buildMST(self):
        """
        Krustal's Minimum Spanning Tree as described by 
            Gautier Marti, Frank Nielsen, Mikołaj Bińkowski, Philippe Donnat, 2017,
            "A review of two decades of correlations, hierarchies, networks and clustering in financial markets" 
        
        The function returns an adjacency matrix.
        """
        # Reset our previous calculations (Set all edges to null)
        self.setProcessedDistanceMatrix()
        # The number of elements in a triangular matrix excluding the diagonal is N(N-1)/2
        for i in range(int((self.node_count * (self.node_count - 1)) / 2)):
            # Add edges in order of increasing distances
            node_a, node_b = self.getIndexOfMinimumDist()
            # Check if the nodes are already connected by a path; if not, add edges to them
            visited = self.DepthFirstSearch(node_a, [0]*self.node_count)
            if not visited[node_b] == 1:
                self.adjacency_matrix[node_a][node_b] = 1
                self.adjacency_matrix[node_b][node_a] = 1
            # Mark the recently selected node to make sure that we will not select it again.
            self.processed_distance_matrix[node_a][node_b] = self.original_distance_matrix.max() + 1
        
        return self.adjacency_matrix

    def getIndexOfMinimumDist(self):
        """
        This function gets the index of the matrix elements with the minimum distance from each other.
        """
        x = list( (np.where(self.processed_distance_matrix == self.processed_distance_matrix.min())) )
        return x[0][0], x[1][0]

    def setDistanceMatrix(self, distance_matrix):
        """
        :param distance_matrix: A NxN matrix of distances

        This function converts the distance matrix into a numpy array, and checks if the matrix is symmetrical.
        """
        try:
            self.original_distance_matrix = np.array(distance_matrix)
            if not (np.allclose(self.original_distance_matrix, self.original_distance_matrix.T)):
                print('Matrix is not symmetrical. Please try again.')
                self.original_distance_matrix = None
                return 1
        except:
            print('Matrix is not symmetrical. Please try again.')
            return 1
        self.original_distance_matrix = np.array(distance_matrix)
        self.setProcessedDistanceMatrix()

    def setProcessedDistanceMatrix(self):
        """
        This function initializes the:
            1. Adjacency Matrix filled with zeros
            2. Distance Matrix with the bottom triangle filled with large distances. This 
               forces the MST algorithm to use only the top triangle and thus avoiding redundancies.
        """
        self.processed_distance_matrix = self.original_distance_matrix
        self.node_count = self.original_distance_matrix.shape[0]
        self.processed_distance_matrix[np.tril_indices(self.node_count, 0)] = self.original_distance_matrix.max() + 1
        self.adjacency_matrix = np.zeros(shape=(self.node_count,self.node_count))