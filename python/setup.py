from setuptools import setup, find_packages


setup(
    name='euler',
    version='1.0.0',
    packages=find_packages('src'),

    author='Austin Bingham',
    author_email='austin@sixty-north.com',
    description='Python solutions to project euler',
    license='MIT',
    keywords='',
    url='http://github.com/abingham/project_euler',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    platforms='any',
    include_package_data=True,
    package_dir={'': 'src'},
    # package_data={'euler': . . .},
    install_requires=[],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest', 'wheel'],
        # 'doc': ['sphinx', 'cartouche'],
        'test': ['hypothesis', 'pytest'],
    },
    entry_points={
    },
)
