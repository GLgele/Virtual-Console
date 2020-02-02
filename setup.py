#-*- coding:utf-8 -*-

####################################################
# File Name: setup.py
# Author: GLgele
# Mail: ai_minecraft@163.com + GLgele@outlook.com
# Created Time:  2020/2/2 13:03:38
####################################################


from setuptools import setup, find_packages

setup(
    name = "VC_cn",
    version = "1.0.0",
    keywords = ("pip","VC_cn"),
    description = "Virtual Console",
    long_description = "Virtual Console on Python",
    license = "None",

    url = "https://github.com/GLgele/Virtual-Console-cn",
    author = "GLgele",
    author_email = "ai_minecraft@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
