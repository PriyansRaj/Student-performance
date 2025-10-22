from setuptools import find_packages,setup
from typing import List

HYPTEN_E_DOT = "-e ."
def get_requirements(filepath:str)->List[str]:
    requirements =[]
    with open(filepath,'r') as f:
        requirements = [req.replace("\n","") for req in f.readlines()]
    
    if HYPTEN_E_DOT in requirements:
        requirements.remove(HYPTEN_E_DOT)

    return requirements
setup(
    name="mlproject",
    version="0.0.1",
    author='Priyans',
    author_email='230701403@rajalakshmi.edu.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
