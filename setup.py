from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="MLOPS-PROJECT1",
    version="0.1",
    author="Harshvardhan",
    packages=find_packages(),
    install_requires = requirements,
)