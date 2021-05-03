import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S1RSB1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# NDIS Guidance Application for Royal Society for the Blind\r\n\r\n### Docassemble\r\n\r\nThis Docassemble package contains the source code and other resources used \r\nwithin the NDIS Guidance Service tool created for RSB.\r\n\r\n### Overview\r\n\r\nWe have been consulted by Sarah (‘the client’), an Adaptive Technology Specialist Trainer at the Royal Society for the Blind (‘RSB’) to provide an application that will assist NDIS clients in understanding their plan, knowing what funds they have and how best to spend these funds.\r\n\r\nThis application was created in collaboration with students from LLAW3301: Law in a Digital Age and COMP3751: Interactive Computer Systems.\r\n\r\n### Authors\r\n- Abigail Groocock\r\n- Jeremy Webster\r\n- Josephine Khoury \r\n- Kolby Gibbs \r\n- Nick Pepaj',
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S1RSB1/', package='docassemble.LLAW33012021S1RSB1'),
     )

