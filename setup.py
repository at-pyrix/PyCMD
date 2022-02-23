import setuptools

name = "pycmd-cli"
description = "PyCmd is a command-line tool to help you manage** your projects"
version = '1.2.7'
readme = open("README.md", "r", encoding="utf8").read()
cli_name = "pycmd"

with open("requirements.txt", "r", encoding="utf8") as f:
    required = f.read().replace("==", ">=").splitlines()
    f.close()

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=[cli_name, f"{cli_name}.commands", f"{cli_name}.utils"],
    keywords=[name, cli_name],
    python_requires=">=3.6",
    license="MIT",
    install_requires=required,
    entry_points=f"[console_scripts]\n{cli_name}={cli_name}.__main__:main",
    include_package_data=True,
)

# python -m pip install wheel twine