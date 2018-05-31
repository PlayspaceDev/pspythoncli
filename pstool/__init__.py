#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2018 - Playspace
import sys
from pspylib.tools import main_tool
from pspylib.common import PackageInfo

__origin__ = "git@gitlab.playspace.com:tools/pstool.git"
__package_name__ = "pstool"

def main():
    packageInfo = PackageInfo(__package_name__)
    return main_tool(sys.argv[1:], description=packageInfo.description, author=packageInfo.author, version=packageInfo.version, origin=__origin__)

if __name__ == "__main__":
    sys.exit(main())
