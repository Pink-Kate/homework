def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": int(age)
                    }

                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Помилка: {line.strip()}. формат неправильний")
                    continue
        return cats_info    

    except FileNotFoundError:
        print(f"Файл {path} не знайдено")  
        return []

    except Exception as e:
        print(f"Сталася помилка:{e}")
        return []    

path = 'text_2_2.txt'
cats_info = get_cats_info(path)
print(cats_info)      
