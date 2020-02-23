# splat_testsuite
Testsuite for SPLAT! using python's unittest

Requirements:
* python 3.7 or later

* python libraries: pillow numpy scipy pyssim

    You can typically install this with something like:

    pip3 install pillow numpy scipy pyssim

* the SPLAT! binary must either be in the splat_testsuite directory (or symlinked), or you must set the environment variable SPLAT. For example, using bash
on unix:

    export SPLAT=$HOME/src/splat/src/splat

Then just do:

    ./runtests.py
