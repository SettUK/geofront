from __future__ import with_statement

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from geofront.version import VERSION


def readme():
    with open('README.rst') as f:
        return f.read()


install_requires = [
    'setuptools',
    'Werkzeug >= 0.9',
    'Flask >= 0.10'
]

tests_require = [
    'pytest >= 2.5.0', 'redis'
]

docs_require = [
    'Sphinx >= 1.2',
    'sphinxcontrib-autoprogram'
]

# Install requirements for documentation if it's run by ReadTheDocs.org
if os.environ.get('READTHEDOCS'):
    install_requires.extend(docs_require)


setup(
    name='Geofront',
    version=VERSION,
    description='Simple SSH key management service',
    long_description=readme(),
    author='Hong Minhee',
    author_email='minhee' '@' 'dahlia.kr',
    maintainer='Spoqa',
    maintainer_email='dev' '@' 'spoqa.com',
    license='AGPLv3 or later',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
        'docs': docs_require
    },
    entry_points='''
        [console_scripts]
        geofront-server = geofront.server:main
    ''',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved '
        ':: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: System :: Systems Administration :: Authentication/Directory'
    ]
)