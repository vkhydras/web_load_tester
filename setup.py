"""
Setup script for the load-tester package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="load-tester",  # Hyphenated package name (for pip)
    version="1.0.0",
    description="A terminal-based website load testing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="victorkimaru8@example.com",
    url="hhttps://github.com/vkhydras/web_load_tester.git",
    packages=find_packages(),  
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
    ],
    python_requires=">=3.7",
    install_requires=[
        "aiohttp>=3.8.0",
        "jsonpath-ng>=1.5.0",
    ],
    entry_points={
        "console_scripts": [
            "load-tester=load_tester.main:main",
        ],
    },
    package_data={
        "load_tester": ["**/*.py"],
    },
    include_package_data=True,
)