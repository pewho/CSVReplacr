#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import csvreplacr
 

setup(
    name='CSVReplacr',
    version=csvreplacr.__version__,
    packages=find_packages(),
    author="Pewho Lewok",
    author_email="pewhoo+csvreplacr@gmail.com",
    description="Simple tool to modify/suppress repetitive pattern str on csv files",
    long_description=open('README.md').read(),
    install_requires=['docopt==0.6.2','ulv==0.2-alpha'],
    dependency_links=['git+https://github.com/pewho/Ulv.git'],
    include_package_data=True,
    url='https://github.com/pewho/CSVReplacr',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Tool - CSV",
    ],
    entry_points = {
        'console_scripts': [
            'csvreplacr = csvreplacr:csvreplacr',
        ],
    },
    license="MIT"
)