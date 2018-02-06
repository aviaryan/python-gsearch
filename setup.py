import os
from setuptools import setup


def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	install_requires = [],

	name = "gsearch",
	version = "1.6.0",
	author = "Avi Aryan",
	author_email = "avi.aryan123@gmail.com",
	description = "Google Search unofficial API for Python with no external dependencies",
	keywords = "search-api google python",
	url = "https://github.com/aviaryan/python-gsearch",
	packages=['gsearch'],
	exclude_package_data = {
		'': ['config.json', '__pycache__/*']
	},
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2"
	],
	include_package_data=True, # needed for MANIFEST

	entry_points={
		'console_scripts': [
			'gsearch = gsearch.googlesearch:run',
			# 'series-renamer-config = series_renamer.series_renamer:editConfig',
		],
	}
)
