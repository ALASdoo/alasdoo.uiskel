from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.md').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='alasdoo.uiskel',
      version=version,
      description="Paster template for Diazo theme development",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=["Environment :: Web Environment",
                   "Framework :: Plone",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.6",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      keywords='',
      author='Vilmos Somogyi - ALAS d.o.o.',
      author_email='oss@alasdoo.com',
      url='http://alasdoo.com/',
      license='BSD',
      packages=find_packages('alasdoo'),
      namespace_packages=['alasdoo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'PasteScript',
          'ZopeSkel',
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      diazo_theme = alasdoo.uiskel:PloneAppThemingTemplate
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
      )
