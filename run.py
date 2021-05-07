#!/usr/bin/env python3
"""
TODO: I want to make  program that compiles and executes different types of programming languages.

NOTE: The name of the program is undefined yet, but the main options are 'execute', 'run' (or another :)
NOTE: I already don't know how to recognize errors when trying to execute the command,
    but I believe that is possible to use ML to do that work (concretely: NLP).
"""
import argparse
import sys
import os
from os import path


__author__ = 'Anaxímeno Brito'
__copyright__ = 'Copyright (c) 2021 by ' + __author__
__version__ = '0.2-pre-alpha'
__license__ = 'undefined already'


def print_error(*errors, to_exit: bool = False):
    full_error_msg = ' '.join(errors)
    print(f'run: error: {full_error_msg}')
    if to_exit:
        exit(1)


class File:

    def __init__(self, filename: str):
        self._exists = path.exists(filename)
        if '.' in filename:
            self._name, self._extension = path.splitext(filename)
        else:
            self._name, self._extension = filename, ''
                

    def __str__(self):
        return self.get_name(self.get_extension())

    def get_name(self, ext: str = '') -> str:
        return str(self._name) + str(ext)

    def get_extension(self) -> str:
        return str(self._extension)

    def get_fullname(self) -> str:
        return self.get_name(self.get_extension())

    def existence(self) -> bool:
        return self._exists


class Runner(object):

    def __init__(self, args):
        self.args = args
        self.file = File(args.filename[0])
        if self.file.existence() is False:
            print_error(f'{self.file.get_fullname()!r} was not found!', to_exit=True)

    def execute(self):
        if self.args.python:
            os.system(f'/usr/bin/python3 {self.file.get_fullname()}')
        elif self.args.clang:
            output = self.file.get_name(ext='.tmp.out')
            os.system(f'gcc {self.file.get_fullname()} -o {output}')
            if path.exists(output):
                os.system(f'./{output}')
                # NOTE: Below should be an argparse arguments to keep or eliminate compiled files.
                if True:
                    os.system(f'rm {output}')
        elif self.args.cplusplus:
            print("This part isn't finished!")
        else:
            print_error('The programming language was not chosen!', to_exit=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='run',
        usage='%(prog)s [-h/--help] [--version] {sub-command}',
        epilog='R-U-N %s' % __copyright__
    )
    parser.add_argument(
        '--version', action='version',
        help='show the current version of this program and exits.',
        version='%(prog)s {}'.format(__version__)
    )

    parser.add_argument('filename', nargs=1, help='name of the file.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--clang', action='store_true')
    group.add_argument('-py', '--python', action='store_true')
    group.add_argument('-cpp', '--cplusplus', action='store_true')

    runner = Runner(parser.parse_args())
    runner.execute()
