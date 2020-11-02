############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 302separation        #
#                                          #
############################################

from time import time

class Matrix():

    """
    Class offering matrix printing and computations.
    """

    def __init__(self):
        self._msize = 0
        self._adjacencyMatrix = []
        self._pathMatrix = []

    def showMatrix(self, matrix: list):
        """Print all the list of people.

        Args:
            matrix (list): Matrix to print.
        """

        for line in matrix:
            for i in range(len(line)):
                if i < (len(line)-1):
                    print("{} ".format(line[i]), end='')
                else:
                    print(line[i])

    def createMatrix(self, size: int) -> list:
        """Create a size*size sized matrix and return it.

        Args:
            size (int): Size of the matrix to be created.

        Returns:
            list: The matrix created.
        """

        return [[0 for _ in range(size)] for _ in range(size)]

    def computeAdjacencyMatrix(self, matrix: list, people: list, paires: list):
        """Fill the matrix with 1 if people are connected, 0 otherwise.

        Args:
            matrix (list): Matrix to fill.
            people (list): List of people's name.
            paires (list): List of friends connected.
        """

        for couple in paires:
            matrix[people.index(couple[0])][people.index(couple[1])] = 1
            matrix[people.index(couple[1])][people.index(couple[0])] = 1

    def computeDistance(self, origin: int, dest: int,
                        distance: int, currentPath: list) -> int:
        """Compute and return the minimal distance from 'origin' to 'dest'.

        Args:
            origin (int): The index of the first person.
            dest (int): The index of the person to connect.
            distance (int): The current distance from the first person.
            currentPath (list): Current path from origin to dest.

        Returns:
            int: Minimal distance between origin and dest.
        """

        def areFriends(first: int, second: int) -> bool:
            """Check if first and second are connected.

            Returns:
                bool: True if first and second are connected. False otherwise.
            """

            return self._adjacencyMatrix[first][second] == 1

        if origin == dest:
            return distance
        distance += 1
        newPath = []
        currentPath.append(origin)
        for ipeople in range(self._msize):
            if areFriends(ipeople, origin) and (ipeople not in currentPath):
                newDistance = self.computeDistance(ipeople, dest, distance, currentPath.copy())
                if newDistance > 0:
                    newPath.append(newDistance)
        if len(newPath) == 0:
            return -1
        return min(newPath)

    def computeShortestPathMatrix(self, adjacency: list, pathMatrix: list,
                                    nbpeople: int, maxDistance: int) -> None:
        """Compute each distance between every person
        and fill the matrix with the shortest.

        Args:
            adjacency (list): Binary matrix of people connection.
            pathMatrix (list): Result distances matrix.
            nbpeople (int): Number of people.
            maxDistance (int): Maximum distance to compute.
        """

        self._msize = nbpeople
        self._adjacencyMatrix = adjacency
        self._pathMatrix = pathMatrix
        #
        for i in range(self._msize):
            for j in range(i+1, self._msize):
                distance = self.computeDistance(i, j, 0, [])
                if distance > maxDistance:
                    distance = 0
                elif distance == -1:
                    distance = 0
                pathMatrix[i][j] = distance
                pathMatrix[j][i] = distance
