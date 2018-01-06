from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='ashell',
    version='0.1',
    packages=['ashell'],
    keywords='shell android ashell',
    url='',
    license='',
    author='Roi Meir',
    author_email='',
    description='Add bashrc like functionality to adb',
    long_description=readme(),
    entry_points={'console_scripts': ['ashell=ashell.ashell:main']},
    install_requires=['pexpect'],
    include_package_data=True
)
