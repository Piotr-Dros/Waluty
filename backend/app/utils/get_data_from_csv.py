import csv
from app.utils.data import data as Data
#from data import data as Data
OWNPATH='/home/lenovo/Python/Waluty/CurrenciesData'

def readCurrency(filename):
    dates = []
    values = []

    path=OWNPATH+'/{0}.csv'.format(filename)

    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        for row in reader:
            if len(row) >= 2:  
                values.append(float(row[0]))
                dates.append(row[1])
    lists=Data(dates,values)
    return lists

