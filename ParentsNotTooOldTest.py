import unittest

from ParentsNotTooOld import check_parents_too_old


class TestCheckParentsTooOld(unittest.TestCase):
    def test_both_parents_under_max_age(self):
        individuals = {
            'I1': {'BIRT': '1 JAN 1980'},
            'I2': {'BIRT': '1 JAN 1980'}
        }
        family = {'HUSB': 'I1', 'WIFE': 'I2'}
        self.assertFalse(check_parents_too_old(family, individuals))

    def test_father_over_max_age(self):
        individuals = {
            'I1': {'BIRT': '1 JAN 1950'},
            'I2': {'BIRT': '1 JAN 1980'}
        }
        family = {'HUSB': 'I1', 'WIFE': 'I2'}
        self.assertTrue(check_parents_too_old(family, individuals))

    def test_mother_over_max_age(self):
        individuals = {
            'I1': {'BIRT': '1 JAN 1980'},
            'I2': {'BIRT': '1 JAN 1950'}
        }
        family = {'HUSB': 'I1', 'WIFE': 'I2'}
        self.assertTrue(check_parents_too_old(family, individuals))

    def test_father_missing(self):
        individuals = {
            'I2': {'BIRT': '1 JAN 1980'}
        }
        family = {'WIFE': 'I2'}
        self.assertFalse(check_parents_too_old(family, individuals))

    def test_mother_missing(self):
        individuals = {
            'I1': {'BIRT': '1 JAN 1980'}
        }
        family = {'HUSB': 'I1'}
        self.assertFalse(check_parents_too_old(family, individuals))

    def test_both_parents_missing(self):
        individuals = {}
        family = {}
        self.assertFalse(check_parents_too_old(family, individuals))
