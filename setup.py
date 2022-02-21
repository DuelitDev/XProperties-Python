from setuptools import find_packages, setup


with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="XProperties",
    version="2.0.9",
    description="Cross-Language .properties file parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Duelit",
    author_email="jyoon07dev@gmail.com",
    maintainer="Duelit",
    maintainer_email="jyoon07dev@gmail.com",
    url="https://github.com/Duelit/XProperties",
    packages=find_packages(),
    python_requires=">=3.7",
    keywords=["xproperties"],
    classifiers=[
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False
)


# python setup.py sdist
# python setup.py bdist_wheel
# twine upload .\dist\XProperties-x.x.x-py3-none-any.whl
