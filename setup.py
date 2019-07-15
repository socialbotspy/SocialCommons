from distutils.core import setup

setup(
    name='SocialCommons',
    version='0.1dev',
    packages=['socialcommons',],
    install_requires = [
        'MeaningCloud_python==1.1.1',
        'clarifai==2.5.2',
        'emoji==0.5.1',
        'instapy_chromedriver==2.44',
        'pathlib==1.0.1',
        'plyer==1.4.0',
        'regex==2019.2.7',
        'requests==2.21.0',
        'selenium==3.141.0',
        'setuptools==39.2.0'
    ]
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)


