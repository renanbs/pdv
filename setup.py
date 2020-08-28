from setuptools import setup, find_packages

setup(name='pdv',
      description='PDV',
      long_description='Just a transaction registering service',
      packages=find_packages(exclude=["*tests*"]),
      version='1.0.0',
      install_requires=[
          'Flask==1.1.2',
          'injector==0.16.0',
      ],
      extras_require={
          'dev': [
              'pycodestyle==2.6.0',
              'pytest==6.0.1',
              'pytest-cov==2.10.1',
              'requests-mock==1.8.0',
              'pytest-mock==3.3.1',
              'pytest-sugar==0.9.4',
              'pytest-lazy-fixture==0.6.3',
              'flake8==3.8.3',
          ],
      }
      )
