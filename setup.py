import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-twitter-feed3',
    version='1.2.2',
    packages=['twitter_feed'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to show a Twitter feed.',
    long_description=README,
    url='https://github.com/DJO3/django-twitter-feed3',
    author='Francois Constant, Dave O'Connor',
    author_email='dev@pytools.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        'Django>=1.7',
        'tweepy>=3.1.0',
    ]
)
