from setuptools import setup

setup(
    name='scratch_d',
    version='0.1',
    description='scratch dependency test d',
    packages=['scratch_d'],
    install_requires=[
        'requests[security]>=2.7.0',
        ],
      )
