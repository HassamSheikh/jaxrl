import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

description = ('Implementations of Reinforcement Learning algorithms in Jax.')

setup(
    name='jaxrl',
    version='0.0.5',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ikostrikov/jaxrl',
    author='Ilya Kostrikov',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='reinforcement, machine, learning, research',
    packages=find_packages(),
    install_requires=install_requires,
    license='MIT',
)
