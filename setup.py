#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as req:
    requirements = req.read().splitlines()

setup_requirements = []

test_requirements = []

project_urls = {
    "Github": "https://github.com/zemfrog/zemfrog",
    "Issue Tracker": "https://github.com/zemfrog/zemfrog/issues",
    "Donation": "https://www.patreon.com/aprilahijriyan",
}

setup(
    author="Aprila Hijriyan",
    author_email="hijriyan23@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Zemfrog is a simple framework based on flask for building a REST API quickly.",
    entry_points={
        "console_scripts": [
            "zemfrog=zemfrog.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="zemfrog",
    name="zemfrog",
    packages=find_packages(include=["zemfrog", "zemfrog.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/zemfrog/zemfrog",
    version="1.0.9",
    zip_safe=False,
    project_urls=project_urls,
)
