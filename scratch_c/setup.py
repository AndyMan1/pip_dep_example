from setuptools import setup

setup(
    name='scratch_c',
    version='0.1',
    description='scratch dependency test c',
    packages=['scratch_c'],
    install_requires=[
        'requests[security]>=2.7.0',
        ],
      )
