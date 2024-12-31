from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads requirements from a file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # Ensure '-e .' is excluded if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Omkar',
    author_email='omkarkubal17@gmail.com',
    packages=find_packages(where="src"),  # Adjust to the correct directory
    package_dir={"": "src"},  # Adjust to the correct directory
    install_requires=get_requirements('requirements.txt')
)
