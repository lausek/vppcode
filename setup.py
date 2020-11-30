from setuptools import find_packages, setup

setup(
    name='vpp2code',
    author='lausek',
    version='0.0.1',
    description='generate java code from vpp files',
    url='https://github.com/lausek/vpp2code',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'lark'
    ],
    entry_points={'console_scripts': ['vpp2code=vpp2code.__main__:main']}
)
