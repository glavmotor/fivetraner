from setuptools import find_packages, setup
setup(
    name='fivetraner',
    packages=find_packages(include=['fivetran_wrapper']),
    version='0.1.0',
    url='https://github.com/glavmotor/fivetraner',
    description='Fivetran service API wrapper',
    long_description=open('README.rst').read(),
    author='Dmitry Kravtsov',
    license='MIT',
    install_requires=['requests==2.*', 'error-wrapper==0.9.*'],
    setup_requires=['pytest-runner==5.*'],
    tests_require=['pytest==4.*', 'pylint==2.*', 'requests==2.*',
                   'error-wrapper==0.9.*'],
    test_suite='tests',
)
