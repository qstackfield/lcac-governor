from setuptools import setup, find_packages

setup(
    name="lcac-sdk",
    version="1.0.0",
    description="LCAC Cognitive Integrity SDK",
    author="Atom Labs",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0"
    ],
)
