#!/usr/bin/python3

import unittest
import tempfile
from filefinder import FileFinder
import os.path

class FinderMethodsCase(unittest.TestCase):
    # Using TemporaryDirectory is very convenient, in that it cleans up the directory and its contents once
    # the object is destroyed. That saves us from implementing a tearDown method, too.
    testdir   = tempfile.TemporaryDirectory()
    dirname   = testdir.name

    def setUp(self):
        self.tempfiles = [ os.path.join(self.dirname,f) for f in ('python','python2','python3','python3.9','python_2.7','the_python_snake') ]
        self.matches   = [ os.path.join(self.dirname,f) for f in ('python','python2','python3') ]
        for filename in self.tempfiles:
            with open(filename,'w') as f:
                pass

    def test_find(self):
        ff = FileFinder(self.dirname)
        self.assertEqual(ff.find(['python','python2','python3']),self.matches)

    def test_glob(self):
        ff = FileFinder(self.dirname)
        self.assertEqual(ff.glob(['python','python?']),self.matches)

    def test_search(self):
        ff = FileFinder(self.dirname)
        self.assertEqual(ff.search(['^python[23]?$']),self.matches)

    def test_cant_find(self):
        ff = FileFinder(self.dirname)
        self.assertCountEqual(ff.find(['cobra','rattlesnake']),[])

    def test_not_list(self):
        ff = FileFinder(self.dirname)
        with self.assertRaises(TypeError):
            ff.find('cobra')
        with self.assertRaises(TypeError):
            ff.glob('rattlesnake*')
        with self.assertRaises(TypeError):
            ff.search('^rattlesnakes?$')

if __name__ == '__main__':
    unittest.main(verbosity=2)