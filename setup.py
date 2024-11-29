#setup.py is used to build our projects as package so that we can use it in another projects
from setuptools import find_packages,setup
Hypen_e_dot='-e .'
def get_requirements(file_path):
    #return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements


setup(
name='mlprojects',
version='0.0.1',
author='nikhil',
author_email='nikhil131102@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)