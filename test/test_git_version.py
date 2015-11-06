#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))))))
import pygh


class TestGitVersion(unittest.TestCase):
    '''
    Tests the :class:`pygh.GitVersion` class
    '''

    def check(self, version):
        '''
        Checks that a :class:`pygh.GitVersion` class has been constructed correctly

        :param Version version: the version to check
        '''
        bigger = (0, 2, 4)
        equal = (0, 1, 2)
        smaller = (0, 0, 3)
        self.assertTrue(version.dirty)
        self.assertEqual(equal, version)
        self.assertNotEqual(smaller, version)
        self.assertGreater(bigger, version)
        self.assertGreaterEqual(bigger, version)
        self.assertGreaterEqual(equal, version)
        self.assertLess(smaller, version)
        self.assertLessEqual(smaller, version)
        self.assertLessEqual(equal, version)

    def test_constructor_arguments(self):
        '''
        Tests that the :class:`pygh.GitVersion` class can be constructed with
        a set of arguments
        '''
        self.check(pygh.GitVersion(0, 1, 2, 'abcdef12-dirty'))
        self.check(pygh.GitVersion(0, 1, 2, 'abcdef12', True))

    def test_constructor_tuple(self):
        '''
        Tests that the :class:`pygh.GitVersion` class can be constructed with
        a tuple
        '''
        self.check(pygh.GitVersion((0, 1, 2, 'abcdef12-dirty')))
        self.check(pygh.GitVersion((0, 1, 2, 'abcdef12', True)))

    def test_constructor_version(self):
        '''
        Tests that the :class:`pygh.GitVersion` class can be constructed with
        from another version class
        '''
        self.check(pygh.GitVersion(pygh.GitVersion(0, 1, 2, 'abcdef12-dirty')))
        self.check(pygh.GitVersion(pygh.GitVersion(0, 1, 2, 'abcdef12', True)))

    def test_constructor_string(self):
        '''
        Tests that the :class:`pygh.GitVersion` class can be constructed with
        from a dot-separated string
        '''
        self.check(pygh.GitVersion('0.1.2.abcdef12-dirty'))

    def test_constructor_dict(self):
        '''
        Tests that the :class:`pygh.GitVersion` class can be constructed with
        from a dict
        '''
        self.check(pygh.GitVersion({'major': 0,
                                    'minor': 1,
                                    'patch': 2,
                                    'commit': 'abcdef12-dirty'}))
        self.check(pygh.GitVersion({'major': 0,
                                    'minor': 1,
                                    'patch': 2,
                                    'commit': 'abcdef12',
                                    'dirty': True}))

    def test_bump(self):
        '''
        Tests that a version number can be bumped up correctly
        '''
        version = pygh.GitVersion('0.1.2.abcdef12')
        version.bump('patch')
        self.assertEqual(version, (0, 1, 3))
        version.bump('minor')
        self.assertEqual(version, (0, 2, 0))
        version.bump('major')
        self.assertEqual(version, (1, 0, 0))
