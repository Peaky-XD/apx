from setuptools import setup, find_packages

setup(
    name="apx",
    version="0.1",
    description="Python library for sending HTTP GET requests (Cython-compiled)",
    author="Your Name",
    author_email="x_spoilt@yahoo.com",  
    url="https://github.com/Peaky-XD/apx",
    packages=find_packages(),
    install_requires=[
        "certifi"
        "_socket",
        "ssl",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
