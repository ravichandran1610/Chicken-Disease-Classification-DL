import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification-DL"
AUTHOR_USER_NAME = "ravichandran1610"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "rravii.r@gmal.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python project for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
