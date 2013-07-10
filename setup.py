from setuptools import setup

setup(name='colifrapy',
      version='0.1',
      description='Command Line Framework',
      url='https://github.com/Yomguithereal/colifrapy.git',
      long_description='Colifrapy is a Command Line Framework for Python. Its aim is to provide several tools to build robust and structured command line tools very easily.',
      author='Yomguithereal',
      license='MIT',
      packages=['colifrapy', 'colifrapy.tools'],
      install_requires=[
        'pyyaml',
      ],
      zip_safe=False)