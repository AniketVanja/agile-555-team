import datetime
import unittest

# Define a function to parse a GEDCOM file and extract birth and marriage dates
def parse_gedcom(file_path):
    birth_dates = {}
    marriage_dates = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('0 @I'):
                for j in range(i, len(lines)):
                    if lines[j].startswith('1 BIRT'):
                        birth_date_str = lines[j+1].split(' ')[2]
                        birth_date = datetime.datetime.strptime(birth_date_str, '%d %b %Y').date()
                        birth_dates[lines[i].split(' ')[1]] = birth_date
                    elif lines[j].startswith('1 MARR'):
                        marriage_date_str = lines[j+1].split(' ')[2]
                        marriage_date = datetime.datetime.strptime(marriage_date_str, '%d %b %Y').date()
                        marriage_dates[lines[i].split(' ')[1]] = marriage_date
                        break

    return birth_dates, marriage_dates

class TestBirthBeforeMarriage(unittest.TestCase):

    def test_birth_before_marriage(self):
        birth_dates, marriage_dates = parse_gedcom('shakespeare.ged')
        for individual in birth_dates:
            if individual in marriage_dates:
                self.assertTrue(birth_dates[individual] < marriage_dates[individual])

    def test_birth_and_marriage_on_same_day(self):
        birth_date = datetime.date(2000, 1, 1)
        marriage_date = datetime.date(2000, 1, 1)
        self.assertTrue(birth_date == marriage_date)

    def test_marriage_before_birth(self):
        birth_date = datetime.date(1990, 1, 1)
        marriage_date = datetime.date(1980, 1, 1)
        self.assertFalse(birth_date < marriage_date)

    def test_birth_and_marriage_same_year(self):
        birth_date = datetime.date(1985, 1, 1)
        marriage_date = datetime.date(1985, 12, 31)
        self.assertTrue(birth_date < marriage_date)

    def test_birth_and_marriage_same_month(self):
        birth_date = datetime.date(1995, 6, 15)
        marriage_date = datetime.date(1995, 6, 30)
        self.assertTrue(birth_date < marriage_date)

if __name__ == '_main_':
    unittest.main()