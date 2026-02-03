from setuptools import setup, find_packages

setup(
    name="binary-tree-pkg",
    version="0.1.0",
    description="Binary Tree implementation with YAML integration",
    packages=find_packages(),
    install_requires=["PyYAML"],
    python_requires=">=3.8",
)
