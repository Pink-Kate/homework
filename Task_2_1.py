def total_salary(path):
    total_salary = 0
    developer_count = 0

    try: 
        with open(path, 'r', encoding ='utf-8') as file:
            for line in file:
                try:
                  name, salary = line.strip().split(',')
                  salary = float(salary)
                  total_salary += salary
                  developer_count += 1
                except ValueError:
                    print(f"Помилка:{line.strip()}")
                    continue  
        if developer_count > 0:
            average_salary = total_salary / developer_count

            return total_salary, average_salary  
        else:
            return 0, 0             
        
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return 0, 0
    
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0 
    
path = "text_2_1.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")     