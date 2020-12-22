from setuptools import find_packages, setup

setup(
    name='factoryfaker',
    packages=find_packages(),
    version='0.1.0',
    description='Generate faker data for python',
    author='Caio Henrique',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)
