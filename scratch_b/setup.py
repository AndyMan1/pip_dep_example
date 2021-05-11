from setuptools import setup

setup(
    name='scratch_b',
    version='0.1',
    description='scratch dependency test b',
    packages=['scratch_b'],
    install_requires=[
        'cryptography==2.*',
        'pyOpenSSL==19.*',
        ],
      )
