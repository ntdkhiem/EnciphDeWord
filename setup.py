#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup 

setup(
    name = "EnciphDeWord",
    version = "1.0",
    description = "Basic Encryption and Decryption based on www.mastermathmentor.com/mmm/Crypt.ashx",
    
    author = "Khiem Nguyen",
    author_email = "ppkhiemnguyen@gmail.com",
    url = "www.github.com/TopKeingt/EnciphDeWord",
    
    license = "",
    keywords = ["Encrypt","Basic","Decrypt"],
    packages = ["EnciphDeWord"],
    requires = ['prettytable','colortable','bcolors','colored'],
    python_requires = "<=2.7",
    classifiers = [],
    
    zip_safe = False
)
