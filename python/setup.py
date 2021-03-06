#!/usr/bin/env python
1
from distutils.core import setup,Extension,os

setup(name = "yamcha-python",
	version = "0.33",
	author = "Taku Kudo",
	author_email = "taku@chasen.org",
	url = "http://chasen.org/~taku/software/yamcha",
	description = "Yet Another Multipurpose Chunk Annotator",
	py_modules=["YamCha"],
	ext_modules = [	
		Extension("_YamCha",
			["YamCha_wrap.cxx",],
			include_dirs=["/usr/local/include"],
			library_dirs=["/usr/local/lib"],
			libraries=["yamcha","stdc++"])
			])
