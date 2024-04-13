import re
import datetime

def validate_input(data):

    data_list = data.split()
    

    if len(data_list) != 6:
        raise ValueError("Неверное количество данных. Ожидается 6 элементов: фамилия, имя, отчество, дата рождения, номер телефона, пол.")
    
    surname, name, patronymic, birth_date, phone_number, gender = data_list
    

    try:
        datetime.datetime.strptime(birth_date, '%d.%m.%Y')
    except ValueError:
        raise ValueError("Неверный формат даты рождения. Ожидается dd.mm.yyyy.")
    
   
    if not phone_number.isdigit():
        raise ValueError("Неверный формат номера телефона. Ожидается целое беззнаковое число.")
    

    if gender not in ('m', 'f'):
        raise ValueError("Неверный формат пола. Ожидается 'm' или 'f'.")

    return surname, name, patronymic, birth_date, phone_number, gender

def write_to_file(surname, data):

    file_name = f"{surname}.txt"
    try:
        with open(file_name, 'a', encoding='utf-8') as file:
           
            file.write(' '.join(data) + '\n')
    except Exception as e:
        
        print(f"Ошибка при записи в файл: {e}")
        raise

def main():
  
    user_input = input("Введите данные (Фамилия Имя Отчество дата рождения номер телефона пол), разделенные пробелом: ")
    
    try:
       
        surname, name, patronymic, birth_date, phone_number, gender = validate_input(user_input)
        

        write_to_file(surname, [surname, name, patronymic, birth_date, phone_number, gender])
        
        print("Данные успешно записаны в файл.")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
