from setuptools import setup, find_packages

setup(
    name="keyboard-widget",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyGObject>=3.42.0",
    ],
    entry_points={
        'console_scripts': [
            'keyboard-widget=main:main',
        ],
    },
    author="Maruuu1101110",
    author_email="elijahejrosialda@gmail.com",
    description="A customizable keyboard overlay widget for Linux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Maruuu1101110/keyboard-widget",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
) 