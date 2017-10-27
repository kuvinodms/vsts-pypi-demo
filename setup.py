#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = "vsts-cd-manager-demo-retro"
VERSION = "4.0.14"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["msrest>=0.2.0", 'mock']

setup(
    name=NAME,
    version=VERSION,
    description="Python wrapper around some of the VSTS APIs",
    author="Vinod Kumar",    
    author_email="kuvinod@microsoft.com",
    url="https://github.com/kuvinodms/vsts-cd-manager-demo",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)

