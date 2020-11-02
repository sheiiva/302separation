############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 302separation        #
#                                          #
############################################

import sys
from copy import deepcopy

from sources.Matrix import Matrix


class Separation():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._n = 6
        self._p1 = None
        self._p2 = None
        self._people = []
        self._couple = []
        self._adjacency = []
        self._distances = []
        #
        self._matrix = Matrix()

    def parseArguments(self):

        if len(sys.argv) == 3:
            self._n = int(sys.argv[2])
        else:
            self._p1 = sys.argv[2]
            self._p2 = sys.argv[3]

    def parseFile(self, filename: str) -> int:
        """Parse a line into two elements.

        Args:
            filename (str): file to parse.

        Returns:
            int: 84 if error.
        """

        def parseLine(line: str) -> None:

            """Parse a line into two elements.
            """

            line = line.replace('\n', '')
            first, second = line.replace(" is friends with ", ";").split(';')
            self._people.append(first)
            self._people.append(second)
            self._couple.append([first, second])

        def removeDuplicated(elems: list) -> list:
            """Remove duplicated elements in 'elems' and return the result list."""

            return list(set(elems))

        with open(filename) as file:
            for line in file:
                if " is friends with " not in line:
                    print("Error: can't read file. (format)")
                    return 84
                parseLine(line)

        self._people = removeDuplicated(self._people)
        self._people.sort()
        return 0

    def setUpMatrixes(self):
        """Created the _adjacency and _distances matrixes and process computations.
        """

        self._adjacency = self._matrix.createMatrix(len(self._people))
        self._distances = self._matrix.createMatrix(len(self._people))
        self._matrix.computeAdjacencyMatrix(self._adjacency, self._people, self._couple)
        self._matrix.computeShortestPathMatrix(self._adjacency, self._distances, len(self._people), self._n)

    def outputPrinting(self):
        """Process output printing of the results.
        """

        if self._p1 is not None and self._p2 is not None:
            print("Degree of separation between {} and {}: ".format(self._p1, self._p2), end='')
            if self._p1 not in self._people or self._p2 not in self._people:
                print("-1")
            else:
                ifirst = self._people.index(self._p1)
                isecond = self._people.index(self._p2)
                print(self._distances[ifirst][isecond])
        else:
            [print(person) for person in self._people]
            print()
            self._matrix.showMatrix(self._adjacency)
            print()
            self._matrix.showMatrix(self._distances)

    def run(self, filename: str) -> None:
        """Run computations and process output printing.

        Args:
            filename (str): The input file.
        """

        self.parseArguments()
        if self.parseFile(filename) == 84:
            exit(84)
        self.setUpMatrixes()
        self.outputPrinting()
