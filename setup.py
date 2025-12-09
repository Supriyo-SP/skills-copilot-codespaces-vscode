from setuptools import setup, find_packages

setup(
    name="skills-copilot",
    version="1.0.0",
    description="A fully functional CLI application for utilities",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "click>=8.1.7",
    ],
    entry_points={
        'console_scripts': [
            'skills-copilot=src.main:cli',
        ],
    },
    extras_require={
        'dev': [
            'pytest>=7.4.3',
            'pytest-cov>=4.1.0',
        ],
    },
)
