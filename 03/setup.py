from setuptools import setup, find_packages


setup(
        name='print-helpers',
        version='0.1',

        packages=find_packages(),

        entry_points={
            'console_scripts': ['bprint=print_helpers.bprint:main']
        },

        python_requires='>=3.6',
    )
