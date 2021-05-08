#!/usr/bin/env python3
"""
TODO: I want to make  program that compiles and executes different types of programming languages.
NOTE: The name of the program is undefined yet, but the main options are 'execute', 'run' (or another :)

NOTE: I already don't know how to recognize errors when trying to execute the command,
    but I believe that is possible to use ML to do that work (concretely: NLP).
NOTE: Another use of NLP is to predict the language used if no extension were given.
"""
import argparse
import sys
import os
from os import path
from common import print_error


__author__ = 'Anaxímeno Brito'
__copyright__ = 'Copyright (c) 2021 by ' + __author__
__version__ = '0.3-pre-alpha'
__license__ = 'undefined already'


class File(object):

    def __init__(self, filename: str):
        self._exists = path.exists(filename)
        if '.' in filename:
            self._name, self._extension = path.splitext(filename)
        else:
            self._name, self._extension = filename, ''           

    def __str__(self):
        return self.get_fullname()

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
        self.command_args = ' '.join(args.args) if args.args else ''
        if self.file.existence() is False:
            print_error(f'{self.file.get_fullname()!r} was not found!', to_exit=True)

    def execute(self):
        if self.args.python:
            os.system(
                f'/usr/bin/python3 {self.file.get_fullname()} {self.command_args}'
            )
        elif self.args.clang:
            output = '.' + self.file.get_name(ext='.tmp.out')
            os.system(f'gcc {self.file.get_fullname()} -o {output}')
            if path.exists(output):
                os.system(f'./{output} {self.command_args}')
                if self.args.keep_compiled is True:
                    os.system(f'mv {output} {self.file.get_name()}')
                else:
                    os.system(f'rm {output}')
        # TODO: finish the cpp compiling process
        #elif self.args.cplusplus:
        #    print("This part isn't finished!")
        else:
            # TODO: try to predict the language and then do the procedure
            print_error('The programming language was not chosen!', to_exit=True)


def main():
    parser = argparse.ArgumentParser(
        prog='run',
        usage='%(prog)s [-h/--help] [--version] {sub-command}',
        epilog='R-U-N %s' % __copyright__
    )
    parser.add_argument(
        '-v', '--version', action='version',
        help='show the current version of this program and exits.',
        version='%(prog)s {}'.format(__version__)
    )

    parser.add_argument('filename', nargs=1, help='name of the file.')

    # Exclusive arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--clang', action='store_true')
    group.add_argument('-py', '--python', action='store_true')
    #group.add_argument('-cpp', '--cplusplus', action='store_true')

    parser.add_argument('-a', '--args', help='arguments for the execution', nargs='+')
    parser.add_argument('--keep-compiled', 
        help='don\'t delete compiled file on compiled languages',
        action='store_true'
    )

    runner = Runner(parser.parse_args())
    runner.execute()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print_error('No commands were given!')
        print('usage: run {-c/-py/-cpp} {filename} {...} [--h/--help] [-v/--version]')
