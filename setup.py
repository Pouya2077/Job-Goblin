from setuptools import setup, find_packages

setup(
    name="Job_Goblin",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
