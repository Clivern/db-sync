"""
    DB-Sync
    ~~~~~~

    Synchronize Data Between Different Database Schemas

    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
import os


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="db-sync",
    version="1.0.0",
    author="Clivern",
    author_email="hello@clivern.com",
    description="Synchronize Data Between Different Database Schemas",
    license="MIT",
    keywords="sync,mysql,mongodb,elasticsearch",
    url="http://clivern.github.io/db-sync/",
    packages=[],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
    ],
)
