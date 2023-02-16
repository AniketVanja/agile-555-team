import datetime
import unittest

class TestShakespeare(unittest.TestCase):
    
    def test_birth_dates_before_current_date(self):
        today = datetime.date.today()
        with open('shakespeare.ged', 'r') as file:
            for line in file:
                if 'BIRT' in line:
                    try:
                        birth_date = datetime.datetime.strptime(next(file).strip()[6:], '%d %b %Y').date()
                        self.assertLess(birth_date, today)
                    except ValueError:
                        pass
    
    def test_death_dates_before_current_date(self):
        today = datetime.date.today()
        with open('shakespeare.ged', 'r') as file:
            for line in file:
                if 'DEAT' in line:
                    try:
                        death_date = datetime.datetime.strptime(next(file).strip()[6:], '%d %b %Y').date()
                        self.assertLess(death_date, today)
                    except ValueError:
                        pass
    
    def test_marriage_dates_before_current_date(self):
        today = datetime.date.today()
        with open('shakespeare.ged', 'r') as file:
            for line in file:
                if 'MARR' in line:
                    try:
                        marriage_date = datetime.datetime.strptime(next(file).strip()[6:], '%d %b %Y').date()
                        self.assertLess(marriage_date, today)
                    except ValueError:
                        pass
    
    def test_divorce_dates_before_current_date(self):
        today = datetime.date.today()
        with open('shakespeare.ged', 'r') as file:
            for line in file:
                if 'DIV' in line:
                    try:
                        divorce_date = datetime.datetime.strptime(next(file).strip()[6:], '%d %b %Y').date()
                        self.assertLess(divorce_date, today)
                    except ValueError:
                        pass
    
    def test_age_at_death_valid(self):
        with open('shakespeare.ged', 'r') as file:
            for line in file:
                if 'BIRT' in line:
                    try:
                        birth_date = datetime.datetime.strptime(next(file).strip()[6:], '%d %b %Y').date()
                    except ValueError:
                        pass
                elif 'DEAT' in line:
                    try:
                        death_date = datetime.datetime.strptime(next(file).strip()[6:], '%d %b %Y').date()
                        age = (death_date - birth_date).days / 365.25
                        self.assertGreaterEqual(age, 0)
                        self.assertLessEqual(age, 120)
                    except ValueError:
                        pass
    
if __name__ == '_main_':
    unittest.main()