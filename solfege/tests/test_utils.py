# Solfege - free ear training software
# Copyright (C) 2007, 2008, 2011, 2016 Tom Cato Amundsen
# License is GPL, see file COPYING


import unittest
from solfege.utils import string_get_line_at
from solfege import utils


class TestStringGetLineAt(unittest.TestCase):

    def test1(self):
        self.assertEqual(string_get_line_at("abc", 1), "abc")
        self.assertEqual(string_get_line_at("\nabc", 1), "abc")
        self.assertEqual(string_get_line_at("abc\n", 0), "abc")
        self.assertEqual(string_get_line_at("abc\n", 2), "abc")
        self.assertEqual(string_get_line_at("abc\n", 3), "abc")
        self.assertEqual(string_get_line_at("abc\n\n", 3), "abc")
        self.assertEqual(string_get_line_at("abc\n\n", 4), "")
        self.assertEqual(string_get_line_at("abc\n\nx", 4), "")
        self.assertEqual(string_get_line_at("abc\n\nx", 5), "x")
        self.assertRaises(IndexError, string_get_line_at, "", 0)
        self.assertEqual(string_get_line_at("  \n\n   \t \n \t abc \n", 3), "")
        self.assertEqual(string_get_line_at("  \n\n   \t \n \t abc \n", 4), "   \t ")


class TestMisc(unittest.TestCase):

    def test_random_tonika_and_interval_in_key(self):
        for x in range(1000):
            # Interval 6 is tritonus. Only f as lower tone
            v = utils.random_tonic_and_interval_in_key("c'", "c''", [6], "c", "major")
            n = v[0].get_octave_notename()
            self.assertTrue(n in ("f'", "b'", "f''"))
            self.assertEqual(v[1], 6)
        for x in range(1000):
            # Interval 5 is perfect fourth.
            v = utils.random_tonic_and_interval_in_key("c'", "c''", [5], "c", "major")
            n = v[0].get_octave_notename()
            self.assertTrue(n in ("c'", "d'", "e'", "g'"))
            self.assertEqual(v[1], 5)
        for x in range(1000):
            # Interval 4 is major third
            v = utils.random_tonic_and_interval_in_key("c'", "c''", [4], "c", "major")
            n = v[0].get_octave_notename()
            self.assertTrue(n in ("c'", "f'", "g'"))
            self.assertEqual(v[1], 4)
        for x in range(1000):
            # Interval 4 is major third
            v = utils.random_tonic_and_interval_in_key("c'", "c''", [4], "d", "major")
            n = v[0].get_octave_notename()
            self.assertTrue(n in ("d'", "g'", "a'"), n)
            self.assertEqual(v[1], 4)
        for x in range(1000):
            # Interval 2 is major second
            v = utils.random_tonic_and_interval_in_key("c'", "c''", [4], "f", "natural-minor")
            n = v[0].get_octave_notename()
            self.assertTrue(n in ("f'", "gis'", "ais'", "cis'", "dis'"), v[0])
            self.assertEqual(v[1], 4)


suite = unittest.makeSuite(TestStringGetLineAt)
suite.addTest(unittest.makeSuite(TestMisc))
