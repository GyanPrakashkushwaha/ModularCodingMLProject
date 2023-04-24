from setuptools import setup , find_packages
from typing import List


Hypen_e_dot = '-e .'

def get_requirements(filePath:str) -> list[str]:

    requirements = []
    with open(filePath) as file_obj:
        requirements = file_obj.readlines()


    requirements = [req.replace('\n','')  for req in requirements]

    if Hypen_e_dot in requirements:
        requirements.remove(Hypen_e_dot)

    return requirements

setup(
    name='ModularCodingProject',
    version='0.0.1',
    description='ModularCodingProject',
    author='GyanPrakashKushwaha',
    author_email='gyanp7880@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)