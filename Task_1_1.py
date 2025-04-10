from datetime import datetime       

def get_days_from_today(date: str) -> int:
    try:  
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - target_date
        return delta.days
    except ValueError:
        print("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")
        return None
    
print(get_days_from_today("2021-10-09"))  
print(get_days_from_today("2030-01-01"))  
print(get_days_from_today("13.14.2000"))  