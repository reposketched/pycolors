from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pyansicolor",
    version="1.0.0",
    author="Sooryashankar Joy",
    author_email="",  # Add your email if desired
    description="A Python library for ANSI 24-bit (True Color) terminal coloring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pyansicolor",  # Update with your actual repository URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="ansi terminal colors console output formatting",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/pyansicolor/issues",
        "Source": "https://github.com/yourusername/pyansicolor",
        "Documentation": "https://github.com/yourusername/pyansicolor#readme",
    },
) 