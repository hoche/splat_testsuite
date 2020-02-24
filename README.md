# splat_testsuite
Testsuite for SPLAT! using python's unittest

## Requirements:
* python 3.7 or later

* python libraries: pillow numpy scipy pyssim

    You can typically install this with something like:

    pip3 install pillow numpy scipy pyssim

* the SPLAT! binary must either be in the splat_testsuite directory (or symlinked), or you must set the environment variable SPLAT. For example, using bash
on unix:

    export SPLAT=$HOME/src/splat/src/splat

## Running
Just do:

    ./runtests.py

## Test Structure
Under the "test" directory, there is a collection of subdirectories. Each subdirectory represents a set of tests that can be completed by one run of SPLAT!. The \__init\__.py sets up the parameters needed to run SPLAT! and then runs it as the first test. Subsequent tests in that directory are for checking the various artifacts from the run; for instance images may be compared to a stock image, text files may be compared to previously-generated text files, and so on.

## Adding More Tests
New tests may be added to the testsuite by creating a subdirectory under "tests" and adding an \__init\__.py. See the manual for unittest for details, and the current set of tests for examples.

In general, the benchmark for "correct behavior" is the 1.4.2 release of SPLAT!, so the process is to run the equivalent test in that release, copy all the artifacts to your new test directory, and then have your \__init\__.py compare new runs to those.
