import requests
from datetime import datetime

data = current_date = datetime.now().date()
teacher = input()




x = requests.get('https://erp.nttek.ru/api/schedule/legacy/('teacher')')

print(x)