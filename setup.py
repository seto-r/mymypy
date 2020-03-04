import re
from os import path
from typing import List

from setuptools import setup

package_name = "mymypy"

root_dir = path.abspath(path.dirname(__file__))


def _requirements() -> List[str]:
    return [
        name.rstrip()
        for name in open(path.join(root_dir, "requirements.txt")).readlines()
    ]


def _test_requirements() -> List[str]:
    return [
        name.rstrip()
        for name in open(path.join(root_dir, "requirements-test.txt")).readlines()
    ]


with open(path.join(root_dir, package_name, "__init__.py")) as f:
    init_text = f.read()
    license = re.search(r"__license__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)
    author = re.search(r"__author__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)
    author_email = re.search(
        r"__author_email__\s*=\s*[\'\"](.+?)[\'\"]", init_text
    ).group(1)
    url = re.search(r"__url__\s*=\s*[\'\"](.+?)[\'\"]", init_text).group(1)

assert license
assert author
assert author_email
assert url

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=package_name,
    packages=[package_name],
    use_scm_version=True,
    license=license,
    install_requires=_requirements(),
    tests_require=_test_requirements(),
    author=author,
    author_email=author_email,
    url=url,
    description="Run mypy and extract errors from your edited code.",
    long_description=long_description,
    keywords=["mypy"],
    entry_points={"console_scripts": ["mymypy=mymypy.__main__:console_entry"]},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
)
