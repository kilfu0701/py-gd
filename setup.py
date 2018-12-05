import codecs
import os
import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="py-gd",
    version=find_version("py_gd", "__init__.py"),
    author="BoRu Su",
    author_email="kilfu0701@gmail.com",
    description="A tiny package for Google Drive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kilfu0701/py-gd",
    packages=['py_gd'],
    install_requires=[
        'PyYAML>=3.11',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
