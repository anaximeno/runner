#!/usr/bin/env python3
import os
import sys

# Support module for the program
__author__ = 'Anaxímeno Brito'
__copyright__ = 'Copyright (c) 2021 by ' + __author__
__version__ = '0.4-pre-alpha'
__license__ = 'undefined already'


def print_error(*errors, to_exit: bool = False):
    """Show the error message and exits if `to_exit` is set to True."""
    full_error_msg = ' '.join(errors)
    print(f'run: error: {full_error_msg}')
    if to_exit:
        exit(1)


class File(object):
    """File perfil to be executed."""

    def __init__(self, filename: str):
        self._dir, self._fname = os.path.split(filename)
        if '.' in self._fname:
            self._name, self._extension = os.path.splitext(self._fname)
        else:
            self._name, self._extension = self._fname, ''           

    def __str__(self)-> str:
        return self.get_fullpath()

    def get_name(self, ext: str = '') -> str:
        """Returs the name of the file if no `ext` (extension) was entered else 
        returns the name with the extension."""
        return str(self._name) + str(ext)

    def get_extension(self) -> str:
        """Returns the file extension."""
        return str(self._extension)

    def get_dir(self) -> str:
        """Returns the file directory."""
        return str(self._dir)

    def get_fullname(self) -> str:
        """Returns the name of the file with it's extension."""
        return self.get_name(self.get_extension())

    def get_fullpath(self)-> str:
        '''Returns the full path of the file.'''
        return os.path.join(self.get_dir(), self.get_fullname())

    def existence(self) -> bool:
        """Return the existence of the file on its directory."""
        return os.path.exists(self.get_fullpath())


class Procedure(object):

    def __init__(self, file: File, command_args: list = ['']):
        self._file = file
        self.command_args = ' '.join(command_args)
        
        if self._file.existence() is False:
            print_error(f'{self._file.get_fullname()!r} was not found!', to_exit=True)

        self.supported_langs = {
            '.c': self.clang,
            '.py': self.python,
            '.cpp': self.cplusplus
        }

    # NOTE: Why this name? :)
    def predict_lang(self):
        """Tries to determine to programming language of the file."""
        if self._file.get_extension() in self.supported_langs:
            return self.supported_langs[self._file.get_extension()]
        return None

    # TODO: add more languages and configurations
    def python(self, **kwargs):
        """Run a python file."""
        os.system(
            f'/usr/bin/python3 {self._file.get_fullpath()} {self.command_args}'
        )

    def clang(self, keep_compiled: bool = False, **kwargs):
        """Run a C file."""
        output = '.' + self._file.get_name(ext='.tmp.out')
        os.system(f'gcc {self._file.get_fullpath()} -o {output}')
        if os.path.exists(output):
            os.system(f'./{output} {self.command_args}')
            if keep_compiled is True:
                os.system(f'mv {output} {self._file.get_name()}')
            else:
                os.system(f'rm {output}')
    
    def cplusplus(self, keep_compiled: bool = False, **kwargs):
        """Run a C++ file."""
        # TODO: finish the cpp compiling process
        print_error("Working with cpp isn't finished yet!", to_exit=True)

