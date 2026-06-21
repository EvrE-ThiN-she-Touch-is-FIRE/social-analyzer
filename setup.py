#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

from setuptools import setup
from setuptools.command.build_py import build_py

with open('README.rst', 'r') as fh:
    long_description = fh.read()


class BuildPy(build_py):
    def run(self):
        super().run()
        dest = os.path.join(self.build_lib, 'social-analyzer', 'data')
        src = 'data'
        if os.path.isdir(src):
            shutil.copytree(src, dest, dirs_exist_ok=True)


setup(
    name='social-analyzer',
    author='QeeqBox',
    author_email='gigaqeeq@gmail.com',
    description="API, CLI & Web App for analyzing & finding a person's profile across 300+ social media websites (Detections are updated regularly)",
    long_description=long_description,
    version='0.45',
    license='AGPL-3.0',
    url='https://github.com/qeeqbox/social-analyzer',
    packages=['social-analyzer'],
    include_package_data=True,
    scripts=['social-analyzer/social-analyzer'],
    install_requires=['BeautifulSoup4', 'tld', 'termcolor', 'langdetect', 'requests', 'lxml', 'galeodes'],
    package_data={'social-analyzer': ['data/*']},
    python_requires='>=3',
    cmdclass={'build_py': BuildPy},
)