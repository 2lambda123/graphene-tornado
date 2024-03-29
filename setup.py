import ast
import re

from setuptools import find_packages
from setuptools import setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("graphene_tornado/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

tests_require = [
    "coveralls",
    "mock",
    "pytest>=4.4.1",
    "pytest-cov>=2.6.1",
    "pytest-tornado>=0.8.1",
    "tox",
]

setup(
    name="graphene-tornado",
    version=version,
    description="Graphene Tornado integration",
    long_description=open("README.rst").read(),
    url="https://github.com/graphql-python/graphene-tornado",
    author="Eric Hauser",
    author_email="ewhauser@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="api graphql protocol rest relay graphene",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "six>=1.10.0",
        "graphene>=3.0",
        "Jinja2>=2.10.1",
        "tornado>=6.1.0, <7.0",
        "werkzeug",
        "typing_extensions",
    ],
    setup_requires=["pytest", "snapshottest"],
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "apollo-engine-reporting": [
            "json-stable-stringify-python==0.2",
            "protobuf>=3.7.1",
            "tornado-retry-client==0.6.1",
        ],
        "opencensus": ["opencensus>=0.7.3"],
    },
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    python_requires=">=3.6",
)
