from setuptools import setup, find_packages

setup(
    name='cajondesastre',
    version='0.1.0',
    description='python packages to help my life',
    long_description='I would just open("README.md").read() here',
    author='Antonio Mesa Garcia',
    author_email='mesaamesa@gmail.com',
    url='https://github.com/mesaamesa/cajondesastre',
    packages=find_packages(exclude=['ut*', 'appIng']),
)
