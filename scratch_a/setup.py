from setuptools import setup

setup(
    name='scratch_a',
    version='0.1',
    description='scratch dependency test a',
    packages=['scratch_a'],
    install_requires=[
        'requests[security]>=2.7.0',
        ],
      )
