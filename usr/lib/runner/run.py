#!/usr/bin/env python3
from common import File, Procedure, print_error
import argparse
import sys


__author__ = 'Anaxímeno Brito'
__copyright__ = 'Copyright (c) 2021 by ' + __author__
__version__ = '0.5-pre-alpha'
__license__ = 'undefined already'


class Runner(Procedure):

    def __init__(self, argparse):
        self._args = argparse
        super().__init__(File(self._args.filename[0]), self._args.args or [''])

    def execute(self):
        if self._args.python:
            self.python()
        elif self._args.clang:
            self.clang(keep_compiled=self._args.keep_compiled,
                compiler=self._args.compiler[0] if self._args.compiler else 'gcc')
        elif self._args.cplusplus:
            self.cplusplus(keep_compiled=self._args.keep_compiled,
                compiler=self._args.compiler[0] if self._args.compiler else 'g++')
        else:
            # NOTE: This section is incomplete.
            lang, compiler = self.predict_lang()
            if lang:
                lang(keep_compiled=self._args.keep_compiled,
                    compiler=self._args.compiler[0] if self._args.compiler else compiler)
            else:
                print_error('Programming language was not indicated, try to specify the language type!', to_exit=True)


def main():
    """Runs the program."""
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

    ### Exclusive arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--clang', action='store_true')
    group.add_argument('-py', '--python', action='store_true')
    group.add_argument('-cpp', '--cplusplus', action='store_true')

    ### Other arguments
    parser.add_argument('-a', '--args', help='arguments for the execution', nargs='+')
    parser.add_argument('--keep-compiled', 
        help='don\'t delete compiled file on compiled languages',
        action='store_true'
    )
    parser.add_argument('--compiler', help='Determine the compiler to be used', nargs=1)

    run = Runner(parser.parse_args())
    run.execute()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print_error('No commands were given!')
        print('usage: run {-c/-py/-cpp} {filename} {...} [-h/--help] [-v/--version]')


# TODO: I want to make  program that compiles and executes different types of programming languages.
# NOTE: The name of the program is undefined yet, but the main options are 'execute', 'run' (or another :)
# NOTE: I already don't know how to recognize errors when trying to execute the command,
#     but I believe that is possible to use ML to do that work (concretely: NLP).
# NOTE: Another use of NLP is to predict the language used if no extension were given.
