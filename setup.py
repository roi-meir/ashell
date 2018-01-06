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
    license='MIT',
    author='Roi Meir',
    description='Add bashrc like functionality to adb',
    long_description=readme(),
    entry_points={'console_scripts': ['ashell=ashell:main']},
    install_requires=['pexpect'],
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Shells',
        'Topic :: Terminals'
    ]
)
