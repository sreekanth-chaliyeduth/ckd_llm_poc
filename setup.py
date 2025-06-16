from setuptools import setup, find_packages

setup(
    name="ckd-llm-poc",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "python-dotenv",
        "openai",
        "pytest",
        "pytest-asyncio",
        "pytest-playwright",
        "pytest-cov",
        "pytest-html",
        "pytest-metadata",
        "httpx",
        "python-multipart",
    ],
    python_requires=">=3.8",
) 