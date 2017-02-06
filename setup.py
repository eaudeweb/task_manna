# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


version = open('version.txt').read().strip()


setup(
    name='task_manna',
    version=version,
    description="Task manager.",
    long_description=(
        open("README.md").read() + "\n" +
        open("HISTORY.md").read() + "\n"
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Flask",
    ],
    keywords='task manna',
    author='David Bătrânu',
    author_email='david.batranu@eaudeweb.ro',
    url='https://github.com/eaudeweb/task_manna',
    license='GPL-3',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Flask',
    ],
    extras_require={
    },
    entry_points={
       'console_scripts': [
           'task_manna = task_manna.run:run_cli',
        ]
   }

)
