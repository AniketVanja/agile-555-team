class Individual:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.families = []

    def add_family(self, family_id):
        self.families.append(family_id)


class Family:
    def __init__(self, id):
        self.id = id
        self.husband = None
        self.wife = None
        self.children = []
        self.marriage_date = None
        self.divorce_date = None

    def set_husband(self, husband_id):
        self.husband = husband_id

    def set_wife(self, wife_id):
        self.wife = wife_id

    def add_child(self, child_id):
        self.children.append(child_id)

    def set_marriage_date(self, marriage_date):
        self.marriage_date = marriage_date

    def set_divorce_date(self, divorce_date):
        self.divorce_date = divorce_date


def no_bigamy(families, individuals):
    for family_id, family in families.items():
        if family.husband and family.wife:
            for spouse_id in [family.husband, family.wife]:
                spouse_families = individuals[spouse_id].families
                if len(spouse_families) > 1:
                    marriage_dates = []
                    for family_id2 in spouse_families:
                        if family_id2 != family_id:
                            spouse2 = families[family_id2].husband if spouse_id == families[family_id2].wife else \
                            families[family_id2].wife
                            marriage_date = families[family_id2].marriage_date
                            if spouse2 and marriage_date:
                                marriage_dates.append(marriage_date)
                    if marriage_dates and family.marriage_date:
                        for marriage_date in marriage_dates:
                            if (family.marriage_date < marriage_date and not family.divorce_date) or (
                                    family.marriage_date < marriage_date and family.divorce_date and family.divorce_date > marriage_date):
                                print(
                                    f"ERROR: {individuals[spouse_id].name} ({spouse_id}) is married to multiple people at the same time in families {family_id} and {family_id2}")


# Example usage
if __name__ == "__main__":
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
    families["F2"].set_wife("I2")
    families["F2"].set_marriage_date("2019-01-01")
    families["F2"].set_divorce_date("2020-02-01")
    families["F3"].set_husband("I1")
    families["F3"].set_wife("I2")
    families["F3"].set_marriage_date("2022-01-01")
    individuals["I1"].add_family("F1")
    individuals["I1"].add_family("F2")
    individuals["I1"].add_family("F3")
    no_bigamy(families, individuals)
