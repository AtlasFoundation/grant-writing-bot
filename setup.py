from setuptools import setup, find_packages

setup(
    name='grant-writing-bot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'spacy',
        'requests',
        'xstate',
    ],
    entry_points={
        'console_scripts': [
            'grant-writing-bot=main:main',
        ],
    },
)
