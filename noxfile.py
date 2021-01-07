# -*- coding: utf-8 -*-
# Copyright (c) 2021 tandemdude
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os

import nox
from nox import options

PATH_TO_PROJECT = os.path.join(".", "shared_cbuff")
SCRIPT_PATHS = [
    PATH_TO_PROJECT,
    "noxfile.py",
    "docs/source/conf.py",
]

options.sessions = ["format_fix", "test", "sphinx"]


@nox.session()
def test(session):
    session.install("-r", "test_requirements.txt")
    session.run("python", "-m", "pytest", "tests", "--testdox")


@nox.session()
def format_fix(session):
    session.install("black")
    session.install("isort")
    session.run("python", "-m", "black", *SCRIPT_PATHS)
    session.run("python", "-m", "isort", *SCRIPT_PATHS)


# noinspection PyShadowingBuiltins
@nox.session()
def format(session):
    session.run("pip", "install", "-U", "black")
    session.run("python", "-m", "black", *SCRIPT_PATHS, "--check")


@nox.session(reuse_venv=True)
def sphinx(session):
    session.install("-U", "sphinx", "sphinx_rtd_theme")
    session.run(
        "python", "-m", "sphinx.cmd.build", "docs/source", "docs/build", "-b", "html"
    )
