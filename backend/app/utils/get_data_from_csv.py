import csv
from app.utils.data import data as Data
#from data import data as Data
CURRENCIESPATH='/home/piotrek/dev/projects/visualisation/Data/currencies'
#https://data.oecd.org/price/inflation-cpi.htm
INFLATIONPATH='/home/piotrek/dev/projects/visualisation/Data/inflation'

def readCurrency(filename):
    dates = []
    values = []

    path=CURRENCIESPATH+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists

def readinflations(filename):
    dates = []
    values = []

    path=INFLATIONPATH+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists

def readCurrency2022(filename):
    dates = []
    values = []

    path=CURRENCIESPATH+'/Currencies2022'+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists

def readCurrency2014(filename):
    dates = []
    values = []

    path=CURRENCIESPATH+'/Currencies2014'+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists



def readCurrency2004(filename):
    dates = []
    values = []

    path=CURRENCIESPATH+'/Currencies2004-7'+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists


def readCurrency2016_18(filename):
    dates = []
    values = []

    path=CURRENCIESPATH+'/Currencies2016.2018'+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(1/(float(row[0])))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists

def readinflations(filename):
    dates = []
    values = []

    path=INFLATIONPATH+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists
