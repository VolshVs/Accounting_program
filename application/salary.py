def calculate_salary():
    import datetime as d
    today = d.date.today().strftime('%d.%m.%Y')
    return print(f'При вызове функции calculate_salary из '
                 f'файла salary.py дата опять {today}')
