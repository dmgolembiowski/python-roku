from roku import __version__
from setuptools import setup, find_packages
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='python-roku',
    version=__version__,
    description='Client for the Roku media player',
    long_description=readme,
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@gmail.com',
    url='http://github.com/jcarbaugh/python-roku/',
    packages=find_packages(),
    license='BSD License',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)