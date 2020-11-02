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

from sources.ArgumentManager import ArgumentManager


def test_needHelp_h_case():

    argman = ArgumentManager()

    argv = ['binary', '-h']

    assert argman.needHelp(argv) is True


def test_needHelp_help_case():

    argman = ArgumentManager()

    argv = ['binary', '--help']

    assert argman.needHelp(argv) is True


def test_needHelp_wrong_case():

    argman = ArgumentManager()

    argv = ['binary', 'path']

    assert argman.needHelp(argv) is False


def test_checkArgs_wrong_case():

    argman = ArgumentManager()

    argv = ['binary']

    assert argman.checkArgs(argv) == 84


def test_checkArgs_normal_3args_case():

    argman = ArgumentManager()

    argv = ['binary', 'tests/deps/example', '3']

    assert argman.checkArgs(argv) == 0


def test_checkArgs_3args_not_a_int():

    argman = ArgumentManager()

    argv = ['binary', 'tests/deps/example', 'a']

    assert argman.checkArgs(argv) == 84


def test_checkArgs_3args_invalid_path():

    argman = ArgumentManager()

    argv = ['binary', 'no', '2']

    assert argman.checkArgs(argv) == 84


def test_checkArgs_normal_4args_case():

    argman = ArgumentManager()

    argv = ['binary', 'tests/deps/example', 'name', 'name']

    assert argman.checkArgs(argv) == 0


def test_checkArgs_4args_invalid_path():

    argman = ArgumentManager()

    argv = ['binary', 'no', 'name']

    assert argman.checkArgs(argv) == 84
