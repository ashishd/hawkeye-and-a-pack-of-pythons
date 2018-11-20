from setuptools import setup, find_packages


setup(
        name='print-helpers',
        version='0.2',

        description='Awesome print functions.',
        author='Ramit Mittal',
        author_email='ramitmittal.k@gmail.com',
        url='https://github.com/ramitmittal/hawkeye-and-a-pack-of-pythons',
        license='GPLv3+',

        packages=find_packages(),

        entry_points={
            'console_scripts': ['bprint=print_helpers.bprint:main']
        },

        python_requires='>=3.6',
    )
