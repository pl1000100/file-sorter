from setuptools import setup
setup(
    name = 'filesorter',
    version = '0.1.0',
    packages = ['filesorter'],
    entry_points = {
        'console_scripts': [
            'filesorter = filesorter.__main__:main'
        ]
    })
