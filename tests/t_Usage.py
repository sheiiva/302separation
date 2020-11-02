############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 302separation        #
#                                          #
############################################

import pytest

from sources.Usage import Usage


def test_show(capsys):

    Usage()

    redir = capsys.readouterr()
    expected = "\
USAGE\n\
\t./302separation file [n | p1 p2]\n\
DESCRIPTION\n\
\tfile\tfile that contains the list of Facebook connections\n\
\tn\tmaximum length of the paths\n\
\tpi\tname of someone in the file\n"

    assert redir.out == expected
