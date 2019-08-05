import setuptools
from distutils.core import setup

with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SocialCommons',
    version='0.0.4',
    author="Ishan Dutta",
    author_email="ishandutta2007@gmail.com",
    description="Common library for all XPy bots under socialbotspy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['socialcommons',],
    install_requires=dependencies,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
)


