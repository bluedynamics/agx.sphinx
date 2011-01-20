# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from setuptools import setup, find_packages
import sys, os

version = "1.0"
shortdesc ="AGX Sphinx extension"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name="agx.sphinx",
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      keywords="AGX, Code Generator, Sphinx",
      author="BlueDynamics Alliance",
      author_email="dev@bluedynamics.com",
      url="https://svn.plone.org/svn/archetypes/AGX",
      license="GNU General Public Licence",
      packages=find_packages("src"),
      package_dir={"": "src"},
      namespace_packages=["agx"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          ##code-section dependencies
          'agx.flavour.dev',
          'sphinxcontrib-mscgen',
          'repoze.sphinx.autointerface',
          ##/code-section dependencies
      ],
      entry_points="""
      ##code-section entry_points
      ##/code-section entry_points
      """,
      )
