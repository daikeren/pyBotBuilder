from distutils.core import setup

from pip.req import parse_requirements
from pip.download import PipSession

install_reqs = parse_requirements('requirements.txt', session=PipSession())

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='pybotbuilder',
    version='0.0.1',
    packages=['botbuilder', ],
    author='Andy Dai',
    install_requires=reqs,
    description='Python interface for Microsoft BotFramework',
    author_email='daikeren@gmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
