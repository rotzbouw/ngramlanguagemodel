# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["regex"]

setup(
    name="ngramlanguagemodel",
    version="0.0.1",
    author="Thierry Göckel",
    author_email="thierry@strayrayday.lu",
    description="A package allowing creation of character ngram based language models.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rotzbouw/ngramlanguagemodel",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
