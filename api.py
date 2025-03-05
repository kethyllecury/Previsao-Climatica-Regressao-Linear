import requests
import json 
from mongo import BancoMongo

banco = BancoMongo()
db = banco.get_database()

api_key = '*****************'

city = 'Recife'

lang = 'pt'

url = f"http://api.openweathermap.org/data/2.5/weather?q={city},br&lang={lang}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    db.orders.insert_one(data)
    
    print("Dados armazenados em mongodb")
    print(data) 
else:
    print(f"Erro ao acessar a API: {response.status_code}")
