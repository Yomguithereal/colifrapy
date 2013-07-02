from setuptools import setup

setup(name='colifrapy',
      version='0.1',
      description='Command Line Framework',
      url='https://github.com/Yomguithereal/colifrapy.git',
      author='Yomguithereal',
      license='MIT',
      packages=['colifrapy', 'colifrapy.tools'],
      install_requires=[
        'pyyaml',
      ],
      zip_safe=False)