# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
        name='pytools',
        version='0.1.0',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'fabric==1.7.0',
        ]
        )

