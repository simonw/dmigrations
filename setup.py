# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name = 'dmigrations',
    version = "0.3.1",
    packages = [
        'dmigrations',
        'dmigrations.management',
        'dmigrations.management.commands',
        'dmigrations.sqlite3',
        'dmigrations.postgresql',
        'dmigrations.mysql',
        'dmigrations.tests',
    ],
)