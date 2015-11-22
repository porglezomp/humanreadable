from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys
import os

import humanreadable

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='humanreadable',
    version=humanreadable.__version__,
    url='https://github.com/porglezomp/human-readable',
    license='Unlicense',
    author='Caleb Jones',
    tests_require=['pytest'],
    install_requires=[],
    author_email='self@calebjones.net',
    packages=['humanreadable'],
    platforms='any',
)
