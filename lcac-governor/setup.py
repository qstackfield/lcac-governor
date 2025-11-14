from setuptools import setup, find_packages

setup(
    name="lcac-governor",
    version="0.1.0",
    description="LCAC Governor – Cognitive Integrity & Drift Governance Engine",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Quinton Stackfield",
    url="https://github.com/qstackfield/lcac-governor",
    license="Apache-2.0",
    packages=find_packages(where="sdk/python"),
    package_dir={"": "sdk/python"},
    install_requires=[
        "requests>=2.31.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
