from datetime import datetime

# Define the maximum allowed age for parents
MAX_PARENT_AGE = 60


# Define a function to calculate a person's age based on their birth date
def calculate_age(birth_date, current_date):
    return current_date.year - birth_date.year - (
                (current_date.month, current_date.day) < (birth_date.month, birth_date.day))


# Define a function to check if a family has parents who are too old
def check_parents_too_old(family, individuals):
    # Get the IDs of the father and mother from the family record
    father_id = family.get('HUSB', None)
    mother_id = family.get('WIFE', None)

    # Check if both father and mother are present in the family record
    if father_id is None or mother_id is None:
        return False

    # Get the birth dates of the father and mother from their individual records
    father_birth_date = individuals[father_id].get('BIRT', None)
    mother_birth_date = individuals[mother_id].get('BIRT', None)

    # Check if both father and mother have birth dates recorded
    if father_birth_date is None or mother_birth_date is None:
        return False

    # Parse the birth dates as datetime objects
    father_birth_date = datetime.strptime(father_birth_date, '%d %b %Y')
    mother_birth_date = datetime.strptime(mother_birth_date, '%d %b %Y')

    # Calculate the ages of the father and mother based on the current date
    current_date = datetime.now()
    father_age = calculate_age(father_birth_date, current_date)
    mother_age = calculate_age(mother_birth_date, current_date)

    # Check if either parent is older than the maximum allowed age
    if father_age > MAX_PARENT_AGE or mother_age > MAX_PARENT_AGE:
        print("Either parent is older than the maximum allowed age ")
        return True
    else:
        print("Neither parent is older than the maximum allowed age ")
        return False


individuals = {
            'I1': {'BIRT': '1 JAN 1980'},
            'I2': {'BIRT': '1 JAN 1980'}
        }
family = {'HUSB': 'I1', 'WIFE': 'I2'}
print(check_parents_too_old(family, individuals))