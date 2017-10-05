#!/usr/bin/env python3
import os
import re

from setuptools import setup, find_packages


name = None
version = None


def find(haystack, *needles):
    regexes = [(index, re.compile("^{}\s*=\s*'([^']*)'$".format(needle))) for index, needle in enumerate(needles)]
    values = ['' for needle in needles]

    for line in haystack:
        if len(regexes) == 0:
            break

        for rindex, (vindex, regex) in enumerate(regexes):
            match = regex.match(line)
            if match:
                values[vindex] = match.groups()[0]
                del regexes[rindex]
                break

    return values


with open(os.path.join(os.path.dirname(__file__), 'fooster', 'db', 'db.py'), 'r') as db:
    name, version = find(db, 'name', 'version')


setup(
    name=name,
    version=version,
    description='a human-readable, magic database in Python',
    url='https://github.com/fkmclane/python-fooster-db',
    license='MIT',
    author='Foster McLane',
    author_email='fkmclane@gmail.com',
    packages=find_packages(),
    namespace_packages=['fooster'],
)
