from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Barreto",
    description="Pacote para operações básicas com imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.9"
)
