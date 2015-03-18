# -*- coding: utf-8 -*-
from setuptools import setup
execfile("physicalproperty/version.py")

setup(name="physicalproperty",
      version=__version__,
      author="Joshua Ryan Smith",
      author_email="joshua.r.smith@gmail.com",
      packages=["physicalproperty"],
      url="https://github.com/jrsmith3/physicalproperty",
      license="MIT",
      description="Descriptor class for physical property attributes",
      classifiers=["Programming Language :: Python",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Science/Research",
                   "Topic :: Scientific/Engineering :: Physics",
                   "Natural Language :: English", ],
      install_requires=["numpy",
                        "astropy"],)
