import datetime


class GEDCOM:
    def __init__(self, file_path):
        self.individuals = {}
        self.families = {}
        current_id = None  # initialize current_id with None

        with open(file_path, 'r') as file:
            for line in file:
                fields = line.strip().split()
                level, tag, args = int(fields[0]), fields[1], fields[2:]

                if level == 0:
                    if tag == 'INDI':
                        current_id = args[0]
                        self.individuals[current_id] = {'ID': current_id}
                    elif tag == 'FAM':
                        current_id = args[0]
                        self.families[current_id] = {'ID': current_id}
                else:
                    if tag == 'NAME' and current_id is not None:  # add a check for current_id
                        self.parse_individual(current_id, ' '.join(args))
                    elif tag == 'HUSB' and current_id is not None:  # add a check for current_id
                        self.families[current_id]['HUSB'] = args[0]

    def parse_individual(self, individual_id, name):
        self.individuals[individual_id]['NAME'] = name

    def is_divorce_before_death(self, individual_id):
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
        if 'DIV' in family:
            divorce_date = datetime.datetime.strptime(family['DIV'], '%d %b %Y').date()
            if 'DEAT' in husband:
                death_date = datetime.datetime.strptime(husband['DEAT'], '%d %b %Y').date()
                if divorce_date > death_date:
                    return False
            if 'DEAT' in wife:
                death_date = datetime.datetime.strptime(wife['DEAT'], '%d %b %Y').date()
                if divorce_date > death_date:
                    return False

        return True


# Creating a GEDCOM object with the path to the GEDCOM file
gedcom = GEDCOM("C:/Users/Arun Rao Nayineni/SSW_555/sample.ged")

# Check if there is a divorce before death for individual with ID "I3"
if gedcom.is_divorce_before_death("I2"):
    print("There is no divorce before death for individual with ID I2.")
else:
    print("There is a divorce before death for individual with ID I2.")
