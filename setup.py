'''
from distutils.core import setup
setup(name='led',
      version='1.0',
      py_modules=['src.led'],
)

from setuptools import setup

setup(
    name = "led",
    packages = ["src"],
    entry_points = {
        "console_scripts": ['led = src.led:switch_light']
        },
)
'''

from setuptools import setup

setup(
    name = "led",
    packages = ["src"],
    entry_points = {
        "console_scripts": ['led = src.led:switch_light']
        },
)
