from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(

# Define project metadata
    name = "template-project-python",
    version = "0.1",
    description = "Generic python project template",
    author = "Capgemini",
    license = "Commercial",

# Install list of requirements
    install_requires = requirements,

# Include all directories within project with an init.py file
    packages = find_packages(),

# Includes additional files without a .py file ending
    include_package_data = True

)

