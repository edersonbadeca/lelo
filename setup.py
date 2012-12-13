from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='lelo',
      version=version,
      description="Utilities for easy paralellisation of tasks",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python parallel highperformance multicore core thread multithread python2',
      author='Joao S. O. Bueno',
      author_email='jsbueno@simplesconsultoria.com.br',
      url='',
      license='LGPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
