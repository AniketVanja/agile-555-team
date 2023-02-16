US03

from time import monotonic, strptime
import datetime

def US03(key, value):
    if 'BIRT' in value:
        birth_date = value['BIRT']
        birth_date = birth_date.split()
        day = int(birth_date[0])
        month = birth_date[1]
        year = int(birth_date[2]) 
        
        month = int(strptime(month,'%b').tm_mon)
        
        birth_date = datetime.date(year, month, day)
        
        if 'DEAT' in value:
            death_date = value['DEAT']
            death_date = death_date.split()
            day = int(death_date[0])
            month = death_date[1]
            year = int(death_date[2])
            month = int(strptime(month,'%b').tm_mon)
        
            death_date = datetime.date(year, month, day)
            
            if birth_date > death_date:
                print("ERROR: INDIVIDUAL: US03 "+key+" died "+str(death_date)+" before born "+str(birth_date))