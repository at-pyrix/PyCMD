import setuptools

# Make your changes here

name = 'pycmd-cli'
description = 'PyCmd is a command-line tool to help you manage** your projects'
version = open('pycmd/version.txt').read().strip()
readme = open('README.md', 'r', encoding='utf8').read()
cli_name = 'pycmd'

# Do not touch part
# Unless you know what you're doing

with open('requirements.txt', 'r', encoding='utf8') as f:
    required = f.read().replace('==', '>=').splitlines()
    f.close()

setuptools.setup (
 name = name,
 version = version,
 description = description,
 long_description=readme,
 long_description_content_type="text/markdown",
 packages=[cli_name, f'{cli_name}.commands', f'{cli_name}.utils'],
 keywords=[name, cli_name],
 python_requires='>=3.6', 
 license='MIT',
 install_requires = required,
 entry_points=f'''
        [console_scripts]
        {cli_name}={cli_name}.__main__:main
    ''',
include_package_data=True
)

# python -m pip install wheel twine

# To build:
# python setup.py sdist bdist_wheel

# To upload:
# twine upload -r pypi dist/*
# NotYasho


# Updating a version
# Change the version in setup.py and pycmd/__main__.py
# Run pypi-update