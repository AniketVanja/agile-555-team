from prettytable import PrettyTable
#SSW-555-Project-Team2
supported_tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']

def parse_line(line):
    try:
        level, tag, arguments = line.strip().split(" ", 2)
        valid = 'Y' if tag in supported_tags else 'N'
        return level, tag, valid, arguments
    except:
        return None

table = PrettyTable()
table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]

individuals = {}
families = {}

def process_individual(indi_id, indi_data):
    name = None
    gender = None
    birt = None
    deat = None

    for item in indi_data:
        level, tag, valid, args = item
        if tag == "NAME":
            name = args
        elif tag == "SEX":
            gender = args
        elif tag == "BIRT":
            birt = args
        elif tag == "DEAT":
            deat = args

    individuals[indi_id] = (name, gender, birt, deat)

def process_family(fam_id, fam_data):
    husb_id = None
    wife_id = None
    marr = None
    div = None

    for item in fam_data:
        level, tag, valid, args = item
        if tag == "HUSB":
            husb_id = args
        elif tag == "WIFE":
            wife_id = args
        elif tag == "MARR":
            marr = args
        elif tag == "DIV":
            div = args

    families[fam_id] = (husb_id, wife_id, marr, div)

with open("Family-1.ged") as file:
    current_id = None
    current_data = []
    current_type = None

    for line in file:
        result = parse_line(line)
        if result:
            level, tag, valid, args = result

            if tag == "INDI":
                if current_id:
                    process_individual(current_id, current_data)
                current_id = args
                current_data = []
                current_type = "INDI"
            elif tag == "FAM":
                if current_id:
                    process_family(current_id, current_data)
                current_id = args
                current_data = []
                current_type = "FAM"
            else:
                current_data.append((level, tag, valid, args))

for indi_id, indi_data in individuals.items():
    name, gender, birt, deat = indi_data
    alive = "True" if deat is None else "False"
    table.add_row([indi_id, name, gender, birt, deat, alive, deat, None])

for fam_id, fam_data in families.items():
    husb_id, wife_id, marr, div = fam_data
    husband = individuals.get(husb_id, ["N/A", "N/A", "N/A", "N/A"])
    wife = individuals.get(wife_id, ["N/A", "N/A", "N/A", "N/A"])

    husband_alive = "True" if husband[3] is None else "False"
    wife_alive = "True" if wife[3] is None else "False"

    table.add_row([fam_id, husband[0], husband[1], None, None, husband_alive, husband[3], wife[0]])
    table.add_row([fam_id, wife[0], wife[1], None, None, wife_alive, wife[3], husband[0]])

print(table)

