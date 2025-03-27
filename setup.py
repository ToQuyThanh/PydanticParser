from setuptools import setup, find_packages

setup(
    name="output_parser_template",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[  
        "pydantic>=2.0",  
        "setuptools>=42",
        "google-genai>=1.7.0",
        "python-dotenv>=1.1.0"
    ],
    extras_require={
        "dev": ["pytest>=8.1.1"]  #  `pip install -e .[dev]`
    },
    python_requires=">=3.8",
)
