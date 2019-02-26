import subprocess
import unittest
import filecmp
import utils
import sys
import os


"""Test of a run of SPLAT's area plot around Summit Park, UT.
   This uses 1-sec arcs and the default distance."""

class TestObject1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """Set up our paths and the names of the local files we're interested in."""
        curdir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(curdir)
        self.splat = utils.findsplat(curdir)
        self.srtms = os.path.join("/mnt","vault","splat","srtm1")
        self.img = os.path.join(curdir, "coverage.png")

    @classmethod
    def tearDownClass(self):
        #maybe don't remove these if there's an error?
        #os.remove(self.img)
        #os.remove(self.report)
        pass

    # tests start here

    def test_01_runsplat(self):
        """Run SPLAT to generate the files"""
        (imgname, suffix) = os.path.splitext(self.img)
        cmd="-hd -d %s -t tx -L 10.0 -R 100 -o %s" % (self.srtms, imgname)
        splatargs=cmd.split()
        splatargs.insert(0, self.splat)
        print(*splatargs)
        #cp = subprocess.run(splatargs, capture_output=True)
        cp = subprocess.run(splatargs)
        self.assertEqual(cp.returncode, 0)

