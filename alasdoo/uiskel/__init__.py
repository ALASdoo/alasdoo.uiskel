from datetime import date
from zopeskel.base import EASY
from zopeskel.base import EXPERT
from zopeskel.base import get_var
from zopeskel.plone import Plone
from zopeskel.vars import BooleanVar

import copy
import os
import shutil


class PloneAppThemingTemplate(Plone):

    _template_dir = 'templates/diazo_theme'
    help = "This package creates a Diazo theme."
    summary = 'A theme for Diazo.'
    category = "Plone Theme Development"

    required_templates = []
    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'add_profile').default = True
    get_var(vars, 'url').default = ''
    get_var(vars, 'zope2product').default = False

    vars.insert(6, BooleanVar(
        'add_browserlayer',
        title='Register Browserlayer',
        description='Should this package register a browserlayer?',
        modes=(EASY, EXPERT),
        default=True,
        help="""If your package has need of a Browserlayer, set this value to 'True'.
To make browserlayer registered, you need to answer True to the Generic Setup profile registration."""
    ))
    vars.append(BooleanVar(
        'use_i18n',
        title='Use i18n (locales)',
        description='Should this package use i18n?',
        modes=(EASY, EXPERT),
        default=True,
        help="""Using i18n allows you to translate your package.""",
    ))

    def pre(self, command, output_dir, vars):
        """Preprocess variables."""
        super(PloneAppThemingTemplate, self).pre(command, output_dir, vars)

        vars['year'] = date.today().year

        # Set version to repr to avoid IOError
        version = vars.get('version')
        if version:
            vars['version'] = repr(version)

    def post(self, command, output_dir, vars):

        # Set version to repr to avoid IOError
        version = vars.get('version')
        if version:
            vars['version'] = repr(version)

        if vars['add_profile'] in (False, 'False'):
            # if we do not want a profile, remove profile directory and test_setup.py.
            path = os.path.join(output_dir,
                                vars['namespace_package'],
                                vars['package'])
            try:
                shutil.rmtree(os.path.join(path, 'profiles'))
                os.remove(os.path.join(path, 'tests', 'test_setup.py'))
            except OSError, e:
                msg = """WARNING: Error in template rendering:

%s

Your package may have structural problems, please check before using it."""
                self.post_run_msg = msg % str(e)

        elif vars['add_browserlayer'] in (False, 'False'):
            path = os.path.join(output_dir,
                                vars['namespace_package'],
                                vars['package'])
            try:
                os.remove(os.path.join(path, 'profiles', 'default', 'browserlayer.xml'))
            except OSError, e:
                msg = """WARNING: Error in template rendering:

%s

Your package may have structural problems, please check before using it."""
                self.post_run_msg = msg % str(e)

        if str(vars['use_i18n']).strip() in (False, 'False'):
            # Remove the locales directory.
            try:
                shutil.rmtree(os.path.join(output_dir, vars['namespace_package'], vars['package'], 'locales'))
            except OSError, e:
                msg = """WARNING: Error in template rendering:

%s

Your package may have structural problems, please check before using it."""
                self.post_run_msg = msg % str(e)
