import unittest
from contextlib import redirect_stdout
from io import StringIO

from NoBigamy import no_bigamy, Individual, Family


class TestNoBigamy(unittest.TestCase):
    def setUp(self):
        self.individuals = {
            "I1": Individual("I1", "John Smith"),
            "I2": Individual("I2", "Jane Doe")
        }
        self.families = {
            "F1": Family("F1"),
            "F2": Family("F2"),
            "F3": Family("F3")
        }
        self.families["F1"].set_husband("I1")
        self.families["F1"].set_wife("I2")
        self.families["F1"].set_marriage_date("2020-01-01")
        self.families["F2"].set_husband("I1")
        self.families["F2"].set_wife("I2")
        self.families["F2"].set_marriage_date("2019-01-01")
        self.families["F2"].set_divorce_date("2020-02-01")
        self.families["F3"].set_husband("I1")
        self.families["F3"].set_wife("I2")
        self.families["F3"].set_marriage_date("2022-01-01")
        self.individuals["I1"].add_family("F1")
        self.individuals["I1"].add_family("F2")
        self.individuals["I1"].add_family("F3")

    def test_no_bigamy_with_no_errors(self):
        no_bigamy(self.families, self.individuals)
        # No errors should be printed to console, so we don't need to assert anything

    def test_no_bigamy_with_bigamy_error(self):
        # create individuals and families
        individuals = {
            "I1": Individual("I1", "John Smith"),
            "I2": Individual("I2", "Jane Doe")
        }
        families = {
            "F1": Family("F1"),
            "F2": Family("F2"),
            "F3": Family("F3")
        }
        families["F1"].set_husband("I1")
        families["F1"].set_wife("I2")
        families["F1"].set_marriage_date("2020-01-01")
        families["F2"].set_husband("I1")
        families["F2"].set_wife("I3")
        families["F2"].set_marriage_date("2021-01-01")
        families["F3"].set_husband("I1")
        families["F3"].set_wife("I4")
        families["F3"].set_marriage_date("2022-01-01")
        individuals["I1"].add_family("F1")
        individuals["I1"].add_family("F2")
        individuals["I1"].add_family("F3")
        individuals["I3"] = Individual("I3", "Mary Johnson")
        individuals["I4"] = Individual("I4", "Lisa Davis")

        # capture printed output
        with StringIO() as buffer, redirect_stdout(buffer):
            no_bigamy(families, individuals)
            output = buffer.getvalue()

        # check if expected error message is in the output
        expected_error = "John Smith (I1) is married to multiple people at the same time in families F2 and F3"
        self.assertIn(expected_error, output)


if __name__ == "__main__":
    unittest.main()
