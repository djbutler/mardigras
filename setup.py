from setuptools import setup, find_packages

#from os import path
#here = path.abspath(path.dirname(__file__))

setup(
    name='mardigras',
    version='0.0.1',
    description='Video analysis and exploration.',
    url='https://github.com/djbutler/mardigras',
    author='Daniel J Butler',
    author_email='daniel.jaffe.butler@gmail.com',
    license='MIT',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['cython>=0.22','scikit-image'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mardigras=mardigras.command_line:main',
        ]
    },


    # package_data={'sample': ['package_data.dat'],},

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
    #    'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
    #    'Intended Audience :: Developers',
    #    'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
    #    'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
    #    'Programming Language :: Python :: 2',
    #    'Programming Language :: Python :: 2.6',
    #    'Programming Language :: Python :: 2.7',
    #],

    # keywords='sample setuptools development',

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

)
