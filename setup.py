
from setuptools import setup, find_packages

setup(
    name="quicksort_package",
    version="0.1.0",
    description="A package that implements the quicksort algorithm.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=['typing'],
    python_requires=">=3.7",
)
