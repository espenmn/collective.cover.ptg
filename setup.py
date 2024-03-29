from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.cover.ptg',
      version=version,
      description="Trueghallery tile for collective.cover",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='collective cover truegallery',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='https://github.com/collective/collective.cover.ptg',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.cover'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.plonetruegallery',
          'collective.cover' 
      ],
      entry_points="""
      # -*- Entry points: -*-
        
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )


