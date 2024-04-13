from setuptools import setup

from pathlib import Pure
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='append_hostfile',
    version='0.1',
    author='Zaid MK',
    author_email='zmahiri@gmail.com',
    description='A simple Python script to add machines to Linux hostfile',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'python-hosts',
        'argparse',
    ],
)