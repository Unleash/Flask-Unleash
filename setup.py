from setuptools import setup, find_packages


def readme():
    with open('README.md') as file:
        return file.read()

setup(
    name='flask_unleash',
    version='0.1.0',
    url='https://github.com/unleash/unleash-client-python',
    license='MIT',
    author='Ivan Lee',
    author_email='ivanklee86@gmail.com',
    description='Flask extention ',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'UnleashClinet==3.1.0'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7"
    ]
)