from setuptools import setup

setup(
    name="wordsim",
    version="0.1",
    description="A simple wrapper for GloVe pretrained word vectors",
    url="https://github.com/nvnmo/WordSim",
    author="Navin Mohan",
    author_email="navinmohan81@gmail.com",
    license="MIT",
    packages=["wordsim"],
    zip_safe=False,
    install_requires=['numpy']
)