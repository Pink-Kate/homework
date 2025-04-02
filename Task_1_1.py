from datetime import datetime       

def get_days_from_today(date):
    now = datetime.today()
    delta = now - date
    return delta.days
date = datetime(2025,2,12)
date_2 = datetime(2025,6,12)
difference = get_days_from_today(date)
difference_2 = get_days_from_today(date_2)
print(difference) 
print(difference_2)
