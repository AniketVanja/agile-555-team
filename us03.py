##US03

from time import monotonic, strptime
import datetime

def plist():
    ilist = [0 for i in range(7)]
    ilist[5] = []
    return ilist

    
def flist():
    flist = [0 for i in range(6)]
    flist[5] = []
    return flist

def lastName(s):
    temp=''
    for i in s:
        if(i != '/'):
            temp += i
    return temp

def currentDate():
    currDate = str(datetime.date.today())
    return currDate

def convertDateFormat(date):
    temp = date.split()
    if(temp[1] == 'JAN'): temp[1] = '01';
    if(temp[1] == 'FEB'): temp[1] = '02';
    if(temp[1] == 'MAR'): temp[1] = '03';
    if(temp[1] == 'APR'): temp[1] = '04';
    if(temp[1] == 'MAY'): temp[1] = '05';
    if(temp[1] == 'JUN'): temp[1] = '06';
    if(temp[1] == 'JUL'): temp[1] = '07';
    if(temp[1] == 'AUG'): temp[1] = '08';
    if(temp[1] == 'SEP'): temp[1] = '09';
    if(temp[1] == 'OCT'): temp[1] = '10';
    if(temp[1] == 'NOV'): temp[1] = '11';
    if(temp[1] == 'DEC'): temp[1] = '12';
    if(temp[2] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        temp[2] = '0' + temp[2]
    return (temp[0] + '-' + temp[1] + '-' + temp[2])

dateList = []
todayDate = currentDate()

def US03(id, birth_date, death_date):
    if (death_date == 0):
        return
    birth_date = birth_date.split("-")
    byear = int(birth_date[0])
    bmonth = int(birth_date[1])
    bday = int(birth_date[2])

    death_date = death_date.split("-")
    dyear = int(death_date[0])
    dmonth = int(death_date[1])
    dday = int(death_date[2])
    if birth_date > death_date:
        print("ERROR: INDIVIDUAL: US03 "+ id +" died "+str(death_date)+" before born "+str(birth_date))

def Gparse(file_name):
    f = open(file_name,'r')
    personvalue = 0
    famvalue = 0
    pdata = []
    fdata = []
    inddata = plist()
    famdata = flist()
    for line in f:
        s = line.split()
        if(s != []):
            if(s[0] == '0'):
                if(personvalue == 1):
                    pdata.append(inddata)
                    inddata = plist()
                    personvalue = 0
                if(famvalue == 1):
                    fdata.append(famdata)
                    famdata = flist()
                    famvalue = 0
                if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                    pass
                else:
                    if(s[2] == 'INDI'):
                        personvalue = 1
                        inddata[0] = (s[1])
                    if(s[2] == 'FAM'):
                        famvalue = 1
                        famdata[0] = (s[1])
            if(s[0] == '1'):
                if(s[1] == 'NAME'):
                    inddata[1] = s[2] + " " + lastName(s[3])
                if(s[1] == 'SEX'):
                    inddata[2] = s[2]
                if(s[1] in ['BIRT', 'DEAT', 'MARR', 'DIV']):
                    date_id = s[1]
                if(s[1] == 'FAMS'):
                    inddata[5].append(s[2])
                if(s[1] == 'FAMC'):
                    inddata[6] = s[2]
                if(s[1] == 'HUSB'):
                    famdata[1] = s[2]
                if(s[1] == 'WIFE'):
                    famdata[2] = s[2]
                if(s[1] == 'CHIL'):
                    famdata[5].append(s[2])
            if(s[0] == '2'):
                if(s[1] == 'DATE'):
                    date = s[4] + " " + s[3] + " " + s[2]
                    if(date_id == 'BIRT'):
                        inddata[3] = convertDateFormat(date)
                    if(date_id == 'DEAT'):
                        inddata[4] = convertDateFormat(date)
                    if(date_id == 'MARR'):
                        famdata[3] = convertDateFormat(date)
                    if(date_id == 'DIV'):
                        famdata[4] = convertDateFormat(date)
    return pdata, fdata
    
def Main(file_name):
    pdata, fdata = Gparse(file_name)
    pdata.sort()
    fdata.sort()

    #US03
    for person in pdata:
        id = person[0]
        birth_date = person[3]
        death_date = person[4]
        US03(id, birth_date, death_date)


Main('/Users/byy/Desktop/test22.ged')
    