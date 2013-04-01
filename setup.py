from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('alasdoo', 'uiskel', 'docs', 'index.rst'))

setup(
    name='alasdoo.uiskel',
    version='1.0',
    description="Paster template for plone.app.theming theme development",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Vilmos Somogyi - ALAS d.o.o.',
    author_email='oss@alasdoo.com',
    url='http://alasdoo.com',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['alasdoo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Cheetah<=2.2.1',
        'Paste',
        'PasteScript',
        'ZopeSkel',
        'hexagonit.testing',
        'plone.testing',
        'setuptools',
        'unittest2',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [paste.paster_create_template]
    diazo_theme = alasdoo.uiskel:PloneAppThemingTemplate
    """,
)
