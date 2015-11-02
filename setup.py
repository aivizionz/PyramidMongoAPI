import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = ['pyramid', 'WebError', 'pyramid_mongodb', 'pymongo', 'pyramid_chameleon']

setup(name='myapp',
      version='0.0',
      description='myapp',
      long_description=README,
      classifiers=[
                  "Programming Language :: Python",
                  "Framework :: Pyramid",
                  "Database :: MongoDB",
                  "Topic :: Internet :: WWW/HTTP",
                  "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author="Rajesh Mathew",
      author_email='rajeshmathewk@gmail.com',
      url='https://github.com/mathewraj/pyramidmongoapp',
      keywords='web python pyramid mongodb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="myapp",
      entry_points="""\
      [paste.app_factory]
      main = myapp:main
      """,
      paster_plugins=['pyramid'],
      )
