import re
from setuptools import setup

# Parse the version number
version = re.search(
    "^__version__\s*=\s*'(.*)'",
    open('uplink/uplink.py').read(),
    re.M).group(1)

# Use README.md as the full description
with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')

setup(name='uplink',
      version=version,
      description='Note-taking CLI with search feature',
      long_description=long_descr,
      url='https://github.com/mcraig2/uplink',
      author='Mike Craig',
      author_email='mike@michaelcraig.io',
      license='MIT',
      packages=['uplink'],
      install_requires=[
          'Click==7.0',
          'numpy==1.16.4',
          'pandas==0.24.2',
          'python-dateutil==2.8.0',
          'pytz==2019.1',
          'six==1.12.0',
      ],
      entry_points = {
          'console_scripts': ['uplink = uplink.uplink:main']
      },
      zip_safe=False)
