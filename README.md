# Introduction

This repository is designed to serve as a generic python template for Capgemini projects.

# Contents

- [Key Files](#key-files)
    - [Requirements](#requirements)
    - [Settings](#settings)
    - [Setup](#setup)
- [Project Setup](#project-setup)
    - [Environment Setup](#environment-setup)


# Requirements

Every project should have a set of requirements. For simple Python projects, all you
need is a text file with required packages listed line by line.

You can choose whether or not to include the version number for a particular package.
Defining a version number will ensure your code remains stable when packages are updated,
although it will fall to you to update the package versions when necessary.


# Settings

The settings file should contain any project specific configuration and variables.
It is an ideal space to store database connection details and anything that is
unchanging and regularly used.

The example file for this project contains a basic logging setup and layout, which can
be easily adjusted according to your needs.


# Setup

This file contains all the metadata for your project. Most importantly, it is used to
create Python eggs, a single-file importable distribution format. Eggs are Python's
version of Java's Jars; an egg is a "logical structure embodying the release of a
specific version of a Python project, comprising its code, resources,
and metadata" ([Python Packaging Authority](https://github.com/pypa/setuptools/blob/master/docs/formats.txt)).

Python eggs are a way of bundling additional information with a Python project,
that allows the project's dependencies to be checked and satisfied at runtime,
as well as allowing projects to provide plugins for other projects.

There are several binary formats that embody eggs, but the most common is '.egg' zipfile
format, because it's a convenient one for distributing projects.

All of the formats support including package-specific data, project-wide metadata,
C extensions, and Python code.

The easiest way to install and use Python eggs is to use the "Easy Install" Python
package manager, which will find, download, build, and install eggs for you;
all you do is tell it the name (and optionally, version) of the Python project(s)
you want to use.

Python eggs can be used with Python 2.3 and up, and can be built using the setuptools
package (see the Python Subversion sandbox for source code, or the EasyInstall page 
or current installation instructions).


# Project Setup

Every project you work on should have its own virtual environment to avoid conflicts and
dependencies from other projects and allow you to easily manage project requirements.

## Environment Setup

There are a number of virtual environment wrappers that serve this purpose; however,
the recommended wrapper for this project is `virtualenvwrapper` (source documentation
can be found [here](http://virtualenvwrapper.readthedocs.io/en/latest/index.html))

#### Installation

If this is your first time working with Python, ensure you have either `pip` or `conda`
installed.

Once you have done this, you can install the wrapper by running one of the following
commands according to your preferred package management system:

`pip install virtualenvwrapper`  

`conda install virtualenvwrapper`

Before you start using the wrapper, there are a couple of environment variables to set up
which will define where the virtual environments will be stored and the location of your
project directories (optional). Add the following commands to your `.bash_profile` file
and refresh your bash session.

```{bash}
# Set the working and project directories
export WORKON_HOME=<workon directory path>
export PROJECT_HOME=<project directory path>

# Run the virtual environment shell script
source /usr/local/bin/virtualenvwrapper.sh
source $HOME/anaconda3/bin/virtualenvwrapper.sh
```

Note that the location of the wrapper script will vary according to the package used for
its install so choose the correct command for your setup.

#### Usage

New virtual environments will be created in the `WORKON_HOME` directory under their
assigned name. To create a new environment, simply run:

`mkvirtualenv <name>`

To manage a specific virtual environment, run the command:

`workon <environment>`

Your command prompt should now be prefixed with the above environment name in brackets.
Any package management commands you run while in this mode will be applied solely to the
active environment.

You can either install packages one by one in the same way as any other package management
tool or you can install a set of packages from a text file. Using pip with this project
requirements file as an example, the command to install and update all the listed
packages:

`pip install --upgrade -r requirements.txt`

The `r` tag tells pip to expect a file from which to extract a list of requirements.

To install another project as a package, ensure it has a setup file which defines the
project name, version and packages. Then navigate to the target project directory and run:

`pip install .`

You will then be able to use any methods and functions within the target project whilst
working on your current virtual environment.
