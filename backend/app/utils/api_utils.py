import requests
import json
from data import data

class apiNBP:
    def getFormApi(self,currency):
        dates=[]
        exchange_rates=[]
        for i in range (2003,2008):
            #print(i)
            for j in range (1,13):
                if i==2023 and j==5:
                    break
                if j>9:
                    url='http://api.nbp.pl/api/exchangerates/rates/a/{2}/{0}-{1}-01/{0}-{1}-28/?format=json'.format(i,j,currency)
                else:
                    url='http://api.nbp.pl/api/exchangerates/rates/a/{2}/{0}-0{1}-01/{0}-0{1}-28/?format=json'.format(i,j,currency)
                
                #print(url)
                response=requests.get(url)
                if response.status_code == 200:
                    #rint(response)
                    data=response.json()
                
                    for k in range(0,len(data['rates'])):
                        dates.append(data['rates'][k]['mid'])
                        exchange_rates.append(data['rates'][k]['effectiveDate'])
        
        

        print(dates)
        print(exchange_rates)
        data=data(dates,exchange_rates)

        return data

    def getGBP(self):
        print(self.getFormApi('gbp'))
    
    def getUSD(self):