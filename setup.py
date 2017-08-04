#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for defbot.

    This file was generated with PyScaffold 2.5.7, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup

setup(name='defbot',
        version='0.1',
        description='automated sentiment analysis bot for reddit',
        url='https://github.com/jasonh9/defBot',
        author='Jason Huang',
        author_email='jhuang9@mail.sfsu.edu',
        license='MIT',
        packages=['defbot'],
        zip_safe=False)

def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
