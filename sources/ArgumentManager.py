############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 302separation        #
#                                          #
############################################

class ArgumentManager():

    def isFloat(self, elem) -> bool:

        """Expect for elem to be a float."""

        try:
            float(elem)
        except ValueError:
            return False
        else:
            return True

    def isFile(self, filename: str) -> bool:

        """Check if filename is an existing file."""

        try:
            f = open(filename)
        except IOError:
            print("{} is not a valid file".format(filename))
            return False
        else:
            f.close()
            return True

    def checkArgs(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        if len(argv) != 3 and len(argv) != 4:
            print("Error: wrong number of arguments")
            return 84
        if len(argv) == 3 \
            and (self.isFloat(argv[2]) is False or float(argv[2]) < 0):
            print("Error: please retry with -h.")
            return 84
        if self.isFile(argv[1]) is False:
            return 84
        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
