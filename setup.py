from setuptools import setup, find_packages


def readme():
    with open('README.md') as file:
        return file.read()


setup(
    name='flask_unleash',
    version='2.0.0',
    url='https://github.com/Unleash/Flask-Unleash',
    license='MIT',
    author='Ivan Lee',
    author_email='ivanklee86@gmail.com',
    description='Flask extension for unleash-client-python.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'UnleashClient',
        'Flask'
    ],
    python_requres=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)
