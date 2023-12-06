import os
import datetime as d


class Accounting:

    def __init__(self, name):
        self.name = name

    def get_datetime(self):
        today = d.date.today().strftime('%d.%m.%Y')
        return print(f'Сегодня {today}')

    def calculate_salary(self):
        from dirty_main import calculate_salary
        return calculate_salary()

    def get_employees(self):
        from dirty_main import get_employees
        return get_employees()


if __name__ == '__main__':
    name = Accounting(os.getenv('NAME'))
    get_datetime = name.get_datetime()
    name.calculate_salary()
    name.get_employees()
