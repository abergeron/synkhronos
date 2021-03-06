from setuptools import setup

setup(name='synkhronos',
      version='1.0.0',
      description='Theano Extension for Data Parallelism',
      long_description='Documentation at: http://synkhronos.readthedocs.io',
      url='http://github.com/astooke/synkhronos',
      author='Adam Stooke',
      author_email='adam.stooke@gmail.com',
      license='MIT',
      packages=['synkhronos'],
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 3',
                   'Operating System :: Unix',
                   'Operating System :: POSIX :: Linux',
                   'Operating System :: MacOS :: MacOS X'],
      zip_safe=False)
