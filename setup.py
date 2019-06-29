import io

from setuptools import find_packages, setup

with io.open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='flaskr',
    version='1.0.0',
    url='',
    license='BSD',
    maintainer='Lining Bai',
    maintainer_email='bailining@gmail.com',
    description='The book recommendation built in flask',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)