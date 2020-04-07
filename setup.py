import os
from setuptools import setup, find_packages
from pkg_resources import resource_string

from setuptools import setup, find_packages
setup(
    name = "smpp.pdu",
    version = "0.3",
    author = "Roger Hoover",
    author_email = "roger.hoover@gmail.com",
    description = "Library for parsing Protocol Data Units (PDUs) in SMPP protocol",
    license = 'Apache License 2.0',
    packages = find_packages(),
    keywords = "smpp pdu",
    url = "https://github.com/mozes/smpp.pdu",
    py_modules=["smpp.pdu"],
    include_package_data = True,
    zip_safe = False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Networking",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

