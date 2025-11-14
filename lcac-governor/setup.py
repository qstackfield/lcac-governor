from setuptools import setup, find_packages

setup(
    name="lcac-sdk",
    version="1.0.0",
    description="LCAC Governor Python SDK — Cognitive Integrity Engine",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Quinton Stackfield",
    author_email="qstackfield@seedcore.io",
    url="https://github.com/qstackfield/lcac-governor",
    license="Apache-2.0",
    packages=find_packages(where="sdk/python"),
    package_dir={"": "sdk/python"},
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.24.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
