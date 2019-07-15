from distutils.core import setup

with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

setup(
    name='SocialCommons',
    version='0.1dev',
    packages=['socialcommons',],
    install_requires=dependencies,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)


