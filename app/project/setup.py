# setup.py
from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'add_numbers=calculator.cli:main',
        ],
    },
    install_requires=[],
    python_requires='>=3.6',
)