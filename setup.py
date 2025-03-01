import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read() 
    
__version__ = "0.0.0"

REPO_NAME = "Text-summary-Project"
AUTHOR_USERNAME = "Aburummy"
SRC_REPO = "summarizer"
AUTHOR_EMAIL = "yaqubalamin12@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A simple text summarization tool using the Transformers library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)