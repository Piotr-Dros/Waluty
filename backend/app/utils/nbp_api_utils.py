#Module is used for downloading data from NBP API
import time
import requests
import csv
import os 
from app.utils.data import data as Data
#from data import data as Data

class apiNBP:
    def getFormApiToCsv(self,currency):
    
        dates=[]
        exchange_rates=[]
        for i in range (2002,2010):
    
            
            for j in range (1,13):
                if i==2023 and j==5:
                    break
                if j>9:
                    url='http://api.nbp.pl/api/exchangerates/rates/a/{2}/{0}-{1}-01/{0}-{1}-28/?format=json'.format(i,j,currency)
                else:
                    url='http://api.nbp.pl/api/exchangerates/rates/a/{2}/{0}-0{1}-01/{0}-0{1}-28/?format=json'.format(i,j,currency)
                
               
                response=requests.get(url)
                if response.status_code == 200:
                   
                    data=response.json()
                
                    for k in range(0,len(data['rates'])):
                        dates.append(data['rates'][k]['mid'])
                        exchange_rates.append(data['rates'][k]['effectiveDate'])
        
        extension=".csv"
            
        project_path = os.getcwd()  
        target_folder = os.path.join(project_path, "CurrenciesData")  
        filepath = os.path.join(target_folder, currency+extension)  

        os.makedirs(target_folder, exist_ok=True) 

        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['exchange_rates','dates']) 
            rows = zip(dates, exchange_rates)
            writer.writerows(rows)



    

    def saveToCsv(self):
        self.getFormApiToCsv('usd')
        print("USD saved")
        time.sleep(10)
        self.getFormApiToCsv('eur')
        print("EUR saved")
        time.sleep(10)
        self.getFormApiToCsv('rub')
        print("RUB saved")
        time.sleep(10)
        self.getFormApiToCsv('jpy')
        print("JPY saved")
        time.sleep(10)
        self.getFormApiToCsv('chf')
        print("CHF saved")






