from setuptools import setup, find_packages
import sys

if sys.version_info < (3, 7):
    raise RuntimeError("aiohttp-ratelimiter requires python 3.7 or later.")


def get_long_description():
    with open("README.md", encoding="utf-8") as file:
        return file.read()


VERSION = "4.0.1"

setup(
    name="aiohttp-ratelimiter",
    version=VERSION,
    description="A simple rate limiter for aiohttp.web",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/SmartWasteSegregatorAndRoutePlanner/aiohttp-ratelimiter",
    packages=find_packages(),
    install_requires=["aiohttp", "limits"],
    extras_require={
        "extra": ["coredis", "emcache"]
    }
)
