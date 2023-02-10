# TEAM 2 SSW 555E

supported_tags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']

def parse_line(line):
    try:
        level, tag, arguments = line.strip().split(" ", 2)
        valid = 'Y' if tag in supported_tags else 'N'
        return level, tag, valid, arguments
    except:
        return None

with open("Family-1.ged") as file:
    fams_count = 0
    indi_count = 0
    for line in file:
        print("-->", line)
        result = parse_line(line)
        if result:
            level, tag, valid, arguments = result
            if tag == "INDI" and indi_count < 5000:
                indi_count += 1
                print("<--", level, "|", tag, "|", valid, "|", arguments)
            elif tag == "FAMS" and fams_count < 1000:
                fams_count += 1
                print("<--", level, "|", tag, "|", valid, "|", arguments)