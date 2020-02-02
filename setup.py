#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: 
# Created Time:  2020/2/2 13:03:38
#############################################


from setuptools import setup, find_packages

setup(
    name = "VC_cn",
    version = "1.0.0",
    keywords = ("pip","),
    description = "time and path tool",
    long_description = "time and path tool",
    license = "MIT Licence",

    url = "https://github.com/fengmm521/pipProject",
    author = "mage",
    author_email = "mage@woodcol.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
