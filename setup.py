from setuptools import find_packages, setup
#from typing import list

def get_requirements(filepath):

    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

# metadata for this ML app
setup(
name = "mlproject",
version = "0.0.1",
author = "Raj",
author_email = "rachitrawat18@gmail.com",
packages = find_packages(), # automaticlly finds packages we will use or have used
install_requires = get_requirements('requirements.txt')
)