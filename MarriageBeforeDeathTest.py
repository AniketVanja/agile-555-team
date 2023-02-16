import unittest
from MarriageBeforeDeath import GEDCOM


class TestGEDCOMMarriageBeforeDeath(unittest.TestCase):
    def setUp(self):
        self.gedcom_file = GEDCOM("sample.ged")

    def test_marriage_after_husband_death(self):
        self.assertFalse(self.gedcom_file.is_marriage_before_death("@I3@"))

    # def test_marriage_before_husband_death(self):
    #     self.assertTrue(self.gedcom_file.is_marriage_before_death("@I1@"))

    # def test_marriage_before_wife_death(self):
    #     self.assertTrue(self.gedcom_file.is_marriage_before_death("@I2@"))

    def test_marriage_after_wife_death(self):
        self.assertFalse(self.gedcom_file.is_marriage_before_death("@I4@"))

    def test_marriage_before_wife_death(self):
        self.assertFalse(self.gedcom_file.is_marriage_before_death("@I3@"))

    def test_marriage_before_husband_death(self):
        self.assertFalse(self.gedcom_file.is_marriage_before_death("@I4@"))

    def test_no_marriage(self):
        self.assertFalse(self.gedcom_file.is_marriage_before_death("@I5@"))


if __name__ == '__main__':
    unittest.main()
