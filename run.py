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


__author__ = 'Anaxímeno Brito'
__copyright__ = 'Copyright (c) 2021 by ' + __author__
__version__ = '0.1-pre-alpha'
__license__ = 'undefined already'


# NOTE: The code already made do not correspond to the real implementation of the program wanted,
# so it is just a test of the ideas.
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


    '''
    subparser = parser.add_subparsers(dest='subparser', title='Sub Command')
    python = subparser.add_parser(
        'py', 
        help='run a python file',
        description='run a python file',
        usage='run py [filename] {--args arguments}'
    )
    python.add_argument('filename', help='name of the file')
    python.add_argument('-a', '--args',
        help='Arguments to the execution',
        nargs='+'
    )


    clang = subparser.add_parser(
        'c',
        help='run a c file',
        description='run a c file',
        usage='run c [filename] {--args arguments}'
    )
    clang.add_argument('filename', help='name of the file')
    clang.add_argument('-a', '--args', help='Arguments to the execution', nargs='+')


    if len(sys.argv) > 1:
        args = parser.parse_args()
        subarg = args.subparser
        if subarg == 'py':
            if type(args.args) == list:
                arguments = ' '.join(args.args)
            else: arguments = args.args
            os.system(f'/usr/bin/python3 {args.filename} {arguments}')
        elif subarg == 'c':
            name, ext = os.path.splitext(args.filename)
            os.system(f'gcc {name+ext} -o {name}')
            if os.path.exists(name):
                if type(args.args) == list:
                    arguments = ' '.join(args.args)
                else: arguments = args.args
                os.system(f'./{name} {args.args} && rm {name}')
    else:
        print("No args were given!")
    '''

    parser.add_argument('-c', '--clang', nargs=1, metavar='filename')
    parser.add_argument('-py', '--python', nargs=1, metavar='filename')

    a = parser.parse_args()

    if a.python:
        if os.path.exists(a.python[0]):
            os.system(f'/usr/bin/python3 {a.python[0]}')
        else:
            print(f'{a.python[0]!r} was not found!')
    elif a.clang:
        if os.path.exists(a.clang[0]):
            name, ext = os.path.splitext(a.clang[0])
            tmp = 'xtmp000'
            os.system(f'gcc {name+ext} -o {tmp}')
            if os.path.exists(tmp):
                os.system(f'./{tmp} && rm {tmp}')
        else:
            print(f'{a.clang[0]!r} was not found!')
