from datetime import datetime       

def get_days_from_today(date):
    try:  
       date = datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
       return "Неправильний формат дати. Використовуйте формат 'ДД.ММ.РРРР'."
    
    now = datetime.today()
    delta = now - date
    return delta.days
date =  "12.02.2025"
date_2 =  "12.06.2025"
date_3 = "13.14.2000"
difference = get_days_from_today(date)
difference_2 = get_days_from_today(date_2)
difference_3 = get_days_from_today(date_3)
print(difference) 
print(difference_2)
print(difference_3)
