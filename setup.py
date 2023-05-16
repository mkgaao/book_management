from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in book_management/__init__.py
from book_management import __version__ as version

setup(
	name="book_management",
	version=version,
	description="Book Management System",
	author="Sid",
	author_email="Administrator",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
