from setuptools import setup

requires = [
    'pytest==2.7.2'
]

setup(
    name='checkers',
    url='https://github.com/tomekstasik/checkers',
    version='1.0',
    description='Checkers game',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=requires
)