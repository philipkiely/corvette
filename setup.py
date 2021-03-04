import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="corvette",
    version="0.1.2",
    author="Philip Kiely",
    author_email="philip@kiely.xyz",
    description="An autoindex static site generator for directory listings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philipkiely/corvette",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
