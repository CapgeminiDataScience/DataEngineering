
from setuptools import setup, find_packages

with open("requirements.txt") as file:
    main_requirements = file.read().splitlines()

with open("test/requirements.txt") as file:
    test_requirements = file.read().splitlines()

setup (

    # Define project metadata
    name         = "template-project-python",
    version      = "0.1",
    license      = "Commercial",
    description  = "Generic python project template",
    url          = "https://bitbucket.org/rhiannajayne/template-project-python/wiki/Home",
    author       = "Rhianna Tomlinson (Capgemini)",
    author_email = "rhianna.a.tomlinson@capgemini.com",
    long_description = "This repository is designed to serve as a generic python template for Capgemini projects",

    # Install list of requirements
    install_requires = main_requirements,

    # Include all directories within project with an init file
    packages = find_packages(),

    # Include additional files matching a given pattern, using the relevant package as the key
    package_data = {"": ["*.md", "*.rst"], "test": ["*.txt"]},

    # Specify a test class or package with associated requirements
    test_suite = "test",
    test_require = test_requirements,

    # Define the methods to be surfaced as part of you package
    entry_points = {"console_scripts": ["template = main:main"]}
    # entry_points = {'setuptools.installation': ['eggsecutable = main:main']}
)
