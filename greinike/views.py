from django.http import HttpResponse
import json
import requests
from datetime import datetime

dia = str(datetime.date(datetime.now()))[8:10]
mes = str(datetime.date(datetime.now()))[5:7]
año = str(datetime.date(datetime.now()))[0:4]
diaActual = dia + "-" + mes + "-" + año
mesActual = "01" + "-" + str(int(mes) - 1) + "-" + año
diaAnterior = str(int(dia) - 1) + "-" + mes + "-" + año

class mindicador:

  def __init__(self, indicador, date):
    self.indicador = indicador
    self.date = date
  
  def InfoApi(self):
    url= f'https://mindicador.cl/api/{self.indicador}/{self.date}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

dolar = str(mindicador("dolar", diaActual).InfoApi()['serie'][0]['valor'])
ipc = str(mindicador("ipc", mesActual).InfoApi()['serie'][0]['valor'])
uf = str(mindicador("uf", diaActual).InfoApi()['serie'][0]['valor'])

#print(datetime.date(datetime.now()))
#datetimeobject = datetime.strptime(str(datetime.date(datetime.now())),'%Y-%m-%d')
#newformat = datetimeobject.strftime('%d-%m-%Y')
#print(newformat)

def inicio(request):
    return HttpResponse(
        dolar + "</br>" + ipc 
    )