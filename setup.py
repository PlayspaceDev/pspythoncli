#!/usr/bin#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2017 - Playspace
#
# Sample CLI tool

from setuptools import setup, find_packages
import os
import sys
import subprocess
import shutil
import json
import pip

from setuptools.command.install import install as _install
from distutils.sysconfig import get_python_lib

import pslib

# ----------------------------------------------------------------------------------------
# Setup Configuration
# ----------------------------------------------------------------------------------------

# Load our configuration
def load_conf():
    config_path = "conf"
    with open(config_path, "r") as json_file:
        return pslib.Bunch(json.load(json_file))
    return pslib.Bunch({})
__conf__ = load_conf()

# ----------------------------------------------------------------------------------------
# Install scripts
# ----------------------------------------------------------------------------------------

class install(_install):
    def run(self):
        pip.main(["install", "-r", "requirements"])
        _install.do_egg_install(self)
        self.execute(_post_install, (self.install_lib,), msg="Running post install task")

def _post_install(install_lib):
    from subprocess import call
    post_install_script = os.path.join(install_lib, __import__('pkg_resources').get_distribution(__conf__.packagename).egg_name()+".egg", __conf__.packagename, __conf__.install)
    if os.path.isfile(post_install_script):
        call([sys.executable, post_install_script, install_lib])
    else:
        print("Skipping custom install script. {install} not found.".format(install=__conf__.install))

# ----------------------------------------------------------------------------------------
# Application entry points
# ----------------------------------------------------------------------------------------

console_scripts = []
console_scripts.append('{cli}={package}:main'.format(cli=__conf__.cliname, package=__conf__.packagename))
if __conf__.console_scripts and len(__conf__.console_scripts) > 0:
    console_scripts += __conf__.console_scripts

setup(
        name=__conf__.packagename,
        version=__conf__.version,
        description=__conf__.description,
        author=__conf__.author,
        packages=find_packages(),
        package_data=__conf__.package_data,
        zip_safe=__conf__.zip_safe,
        entry_points={'console_scripts': console_scripts},
        cmdclass={
            'install': install
        }
)