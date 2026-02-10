#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   setup.py
@Time    :   2026/02/10 12:37:38
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2026, Alejandro Marrero
@Desc    :   None
"""

from glob import glob

from setuptools import Extension, find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()


requirements = []

test_requirements = [
    "pytest>=3",
]


class get_pybind_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked."""

    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11

        return pybind11.get_include(self.user)


compile_args = ["-std=c++11"]
ext_modules = [
    Extension(
        "pisinger_cpp",
        sorted(glob("pisingerpy/src/*.cpp")),
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
            get_pybind_include(user=True),
        ],
        extra_compile_args=compile_args,
        language="c++",
    ),
]

setup(
    packages=find_packages(include=["pisingerpy", "pisingerpy.*"]),
    ext_modules=ext_modules,
)
