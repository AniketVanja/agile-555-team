import datetime


class GEDCOM:
    def __init__(self, file_path):
        self.individuals = {}  # dictionary to store individuals
        self.families = {}  # dictionary to store families

        with open(file_path, 'r') as file:
            for line in file:
                # Parse the GEDCOM file
                # and store individuals and families in the respective dictionaries
                pass

    def is_marriage_before_death(self, individual_id):
        if individual_id not in self.individuals:
            return False

        individual = self.individuals[individual_id]
        if 'FAMS' not in individual:
            return False

        family_id = individual['FAMS']
        if family_id not in self.families:
            return False

        family = self.families[family_id]
        if 'HUSB' not in family or 'WIFE' not in family:
            return False

        husband_id = family['HUSB']
        wife_id = family['WIFE']
        if husband_id not in self.individuals or wife_id not in self.individuals:
            return False

        husband = self.individuals[husband_id]
        wife = self.individuals[wife_id]
        if 'DEAT' in husband:
            death_date = datetime.datetime.strptime(husband['DEAT'], '%d %b %Y').date()
            if 'MARR' in family:
                marriage_date = datetime.datetime.strptime(family['MARR'], '%d %b %Y').date()
                if marriage_date > death_date:
                    return False
        if 'DEAT' in wife:
            death_date = datetime.datetime.strptime(wife['DEAT'], '%d %b %Y').date()
            if 'MARR' in family:
                marriage_date = datetime.datetime.strptime(family['MARR'], '%d %b %Y').date()
                if marriage_date > death_date:
                    return False

        return True
