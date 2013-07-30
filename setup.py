from setuptools import setup

setup(name='colifrapy',
      version='0.2',
      description='Command Line Framework',
      url='https://github.com/Yomguithereal/colifrapy.git',
      long_description=open("./README.md", "r").read(),
      author='Yomguithereal',
      license='MIT',
      packages=['colifrapy', 'colifrapy.tools'],
      install_requires=[
        'pyyaml',
        'pystache'
      ],
      package_data={'colifrapy' : ['colifrapy/templates/*']},
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      colifrapy=colifrapy.scaffolder:main
      """
      )