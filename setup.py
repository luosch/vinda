try:
    from setuptools import setup
except:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name = 'vinda',
    packages = ['vinda'],
    version = '0.2.0',
    description = '`Help users construct their index pages rapidly',
    long_description = readme,
    author = 'Sicheng Luo',
    author_email = 'i@lsich.com',
    url = 'https://github.com/luosch/vinda',
    keywords = ['vinda', 'index', 'html'],
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ]
)