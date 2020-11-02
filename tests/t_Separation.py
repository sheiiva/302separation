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

import pytest

from sources.Separation import Separation
from tests.deps.expected import *

def test_parseFile_normal_case():

    sep = Separation()
    expected = ['Barack Obama', 'Chuck Norris', 'Cindy Crawford',
                'François Hollande', 'Jesus', 'Katie Holmes',
                'Lara Croft', 'Nicole Kidman', 'Penelope Cruiz',
                'Sim', 'Tom Cruise', 'V', 'Yvette Horner']

    res = sep.parseFile("./tests/deps/example")

    assert res == 0
    assert sep._people == expected


def test_parseFile_wrong_separation_case():

    sep = Separation()
    res = sep.parseFile("./tests/deps/wrong_separation")

    assert res == 84


def test_parseFile_duplicated_case():

    sep = Separation()
    expected = ['Barack Obama', 'Chuck Norris', 'Cindy Crawford',
                'François Hollande', 'Jesus', 'Katie Holmes',
                'Lara Croft', 'Nicole Kidman', 'Penelope Cruiz',
                'Sim', 'Tom Cruise', 'V', 'Yvette Horner']

    res = sep.parseFile("./tests/deps/example")

    assert res == 0
    assert sep._people == expected


def test_run_relation_case(capsys):

    sys.argv = ['./302separation', 'tests/deps/example', '3']

    sep = Separation()
    sep.run("./tests/deps/example")

    redir = capsys.readouterr()

    assert redir.out == FULL_EXPECTED


def test_run_yvette_yvette(capsys):

    sys.argv = ['./302separation', './tests/deps/example', 'Yvette Horner', 'Yvette Horner']

    sep = Separation()
    sep.run("./tests/deps/example")

    redir = capsys.readouterr()

    assert redir.out == EXPECTED_YVETTE_YVETTE


def test_run_yvette_mike(capsys):

    sys.argv = ['./302separation', './tests/deps/example', 'Yvette Horner', 'Mike Tyson']

    sep = Separation()
    sep.run("./tests/deps/example")

    redir = capsys.readouterr()

    assert redir.out == EXPECTED_YVETTE_MIKE


def test_run_yvette_barack(capsys):

    sys.argv = ['./302separation', './tests/deps/example', 'Yvette Horner', 'Barack Obama']

    sep = Separation()
    sep.run("./tests/deps/example")

    redir = capsys.readouterr()

    assert redir.out == EXPECTED_YVETTE_BARACK
