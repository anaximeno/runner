"""
Nothing was made yet here!
"""
import sys
import os

# Support module for the program
__author__ = 'Anaxímeno Brito'
__copyright__ = 'Copyright (c) 2021 by ' + __author__
__version__ = '0.3-pre-alpha'
__license__ = 'undefined already'


def print_error(*errors, to_exit: bool = False):
    full_error_msg = ' '.join(errors)
    print(f'run: error: {full_error_msg}')
    if to_exit:
        exit(1)
