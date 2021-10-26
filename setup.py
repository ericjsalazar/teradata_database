import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teradata-database-eric-salazar",
    version="0.0.5",
    author="Eric Salazar",
    author_email="Eric.Salazar@amgreetings.com",
    description="Wrapper package for teradata sql",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/AmericanGreetings/Analytics/_git/teradata_database",
    project_urls={
        "Bug Tracker": "https://dev.azure.com/AmericanGreetings/Analytics/_git/teradata_database",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "sqlalchemy",
        "teradatasql",
        "teradatasqlalchemy"
    ],
)