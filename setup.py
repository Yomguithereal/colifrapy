from setuptools import setup

setup(name='colifrapy',
      version='0.4.0',
      description='Command Line Framework for Python',
      url='http://yomguithereal.github.io/colifrapy/',
      long_description="Colifrapy is a Command Line Framework for Python. Its aim is to provide several tools to build robust and structured command line tools very easily.",
      author='Yomguithereal',
      license='MIT',
      packages=['colifrapy', 'colifrapy.tools'],
      install_requires=['pyyaml', 'argparse'],
      package_data={'colifrapy' : ['colifrapy/templates/*']},
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      colifrapy=colifrapy.scaffolder:main
      """,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Topic :: Software Development :: Code Generators',
            'Topic :: Software Development :: Libraries :: Application Frameworks'
      ]
)
