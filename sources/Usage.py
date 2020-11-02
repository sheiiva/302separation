############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 301dannon            #
#                                          #
############################################

class Usage():

    def __init__(self):
        self.show()

    def show(self) -> None:

        """
        Show usage of the program.
        """

        print(
            "USAGE\n"
            "\t./302separation file [n | p1 p2]\n"
            "DESCRIPTION\n"
            "\tfile\tfile that contains the list of Facebook connections\n"
            "\tn\tmaximum length of the paths\n"
            "\tpi\tname of someone in the file"
            )
