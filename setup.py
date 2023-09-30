from setuptools import setup, find_packages

setup(
    name='your_package',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tkinter'
    ],
    entry_points={
        'console_scripts': [
            'sortify=your_package.main:main'
        ]
    },
)
