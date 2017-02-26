#!/usr/bin/env python
# (c) 2017 Orega S.L.

from distutils.core import setup

setup(
    name='orega',
    version='0.1.0',
    description='Orega S.L. web page project',
    author='Alejandro Otero Ortiz de Cosca',
    author_email='aoterort@gmail.com',
    install_requires=[
        'django==1.10.5',
        'django-cms',
        'django-filer',
        'djangocms-text-ckeditor',
    ],
    extras_require={
        'development': [
        ],
        'test': [],
    }
)
