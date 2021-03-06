from setuptools import setup

setup(
    name = 'omniui',
    version = '1.0.2',
    description = 'A Diagnosis, Analytic and Management Framework for SDN',
    author = 'D-Link NCTU Joint Research Center',
    url = 'https://github.com/dlinknctu/OpenADM',
    install_requires = ['Flask==0.10.1', 'Flask_Cors', 'gevent', 'pymongo', 'flask_socketio'],
    packages = ['src', 'src.floodlight_modules','src.trema_modules','src.pox_modules', 'test'],
    data_files = [('etc', ['etc/config.json'])],
    entry_points = {
        'console_scripts': ['omniui=src.core:main'],
    },
    test_suite = 'test'
)
