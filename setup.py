#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

# For Testing:
#
# python3.4 setup.py register -r https://testpypi.python.org/pypi
# python3.4 setup.py bdist_wheel upload -r https://testpypi.python.org/pypi
# python3.4 -m pip install -i https://testpypi.python.org/pypi
#
# For Realz:
#
# python3.4 setup.py register
# python3.4 setup.py bdist_wheel upload
# python3.4 -m pip install

PY3_DEPS = [
    'six',
    'hexdump',
    'vivisect-vstruct-wb>=1.0.3',
]

# python2.7 has no `functools.lru_cache`,
# so use a backported copy when necessary.
PY2_DEPS = PY3_DEPS + ['functools32']

if sys.version_info[0] == 2:
    DEPS = PY2_DEPS
elif sys.version_info[0] == 3:
    DEPS = PY3_DEPS
else:
    raise RuntimeError('unexpected python major version')

setup(
    name='python-idb',
    version='0.5.0',
    description='Pure Python parser for IDA Pro databases (.idb files)',
    author='Willi Ballenthin',
    author_email='willi.ballenthin@gmail.com',
    url='https://github.com/williballenthin/python-idb',
    license='Apache License 2.0',
    install_requires=DEPS,
    extras_require = {
        # install like `pip install python-idb[disassembly]`
        # note, capstone is annoying to install on windows and in virtualenvs.
        'disassembly':  ['capstone'],
    },
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    entry_points={
        "console_scripts": [
        ]
      },

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],
)
