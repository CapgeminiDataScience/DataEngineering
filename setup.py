from setuptools import setup, find_packages

with open("requirements.txt") as file:
    main_requirements = file.read().splitlines()

with open("test/requirements.txt") as file:
    test_requirements = file.read().splitlines()

setup(

# Define project metadata
    name = "template-project-python",
    version = "0.1",
    description = "Generic python project template",
    author = "Capgemini",
    license = "Commercial",

# Install list of requirements
    install_requires = main_requirements,

# Include all directories within project with an init.py file
    packages = find_packages(),

# Include additional files without a .py file ending, using the relevant package as the key
    package_data = {"": ["*.md", "*.rst"], "test": ["*.txt"]},

# Specify a test class or package with associated requirements
    test_suite = "test",
    test_require = test_requirements

)
