import requests
from datetime import datetime

data = datetime.now().date()
teacher = input()

x = requests.get('https://erp.nttek.ru/api/schedule/legacy/('data')/('teacher')')

print(x)
