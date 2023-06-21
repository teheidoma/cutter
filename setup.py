from setuptools import setup

setup(
    name='cutter',
    version='1.2',
    py_modules=['cutter'],
    install_requires=[
        'ffmpeg-python',
    ],
    entry_points='''
        [console_scripts]
        cutter=cutter:main
        tomp3=cutter:tomp3
    ''',
)