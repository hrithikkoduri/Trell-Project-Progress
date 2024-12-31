from setuptools import setup, find_packages

setup(
    name="content_creation_crew",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)