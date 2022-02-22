import setuptools

# Make your changes here

name = 'pycmd-cli'
description = 'PyCmd is a command-line tool to help you manage** your projects'
version = '1.2.0'
author = 'NotYasho'
author_email = 'wiredhack022@email.com',
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
 author=author,
 author_email=author_email,
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
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*