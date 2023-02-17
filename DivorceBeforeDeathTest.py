import unittest
from DivorceBeforeDeath import GEDCOM


class TestGEDCOM(unittest.TestCase):
    def setUp(self):
        self.gedcom = GEDCOM("C:/Users/Arun Rao Nayineni/SSW_555/sample.ged")

    def test_divorce_after_death(self):
        self.assertFalse(self.gedcom.is_divorce_before_death("I1"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I2"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I3"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I4"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I5"))

    def test_divorce_before_death3(self):
        self.assertFalse(self.gedcom.is_divorce_before_death("I1"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I2"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I3"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I4"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I5"))

    def test_divorce_before_death(self):
        self.assertFalse(self.gedcom.is_divorce_before_death("I1"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I2"))
        self.assertFalse(self.gedcom.is_divorce_before_death("I3"))

    def test_no_marriage(self):
        self.assertFalse(self.gedcom.is_divorce_before_death("I3"))


if __name__ == '__main__':
    unittest.main()
