from setuptools import setup, find_packages

version = '0.1'

setup(name='Cert Check',
      version=version,
      description="Serve apple space content",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='Srikanth',
      author_email='sri',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pyOpenSSL'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      certchecker = checker.check:main
      """,
      )

