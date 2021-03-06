from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rosmake'],
    package_dir={'': 'src'},
    scripts=['scripts/rosmake'],
    requires=['rospkg']
)

setup(**d)
