import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        return sum(record.amount for record in self.records if record.date == dt.datetime.now().date())      
    
    def get_week_stats(self):
        present_day = dt.datetime.now().date()
        delta = dt.timedelta(days=7)
        week_stats = 0
        first_date = present_day - delta
        for record in self.records:
            if first_date < record.date <= present_day:
                week_stats += record.amount
        return week_stats

    def get_difference(self):
        subtraction = self.limit - self.get_today_stats()
        return subtraction
        

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if Calculator.get_difference(self) > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, ' 
                f'но с общей калорийностью не более '
                f'{self.get_difference()} кКал')

        return 'Хватит есть!'


class CashCalculator(Calculator):

    USD_RATE = 60.00
    EURO_RATE = 70.00
    RUB_RATE = 1.00
    currencies = {
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro'),
        'rub': (RUB_RATE, 'руб')
        }

    def get_today_cash_remained(self, currency):

        if currency not in self.currencies:
            return f'Валюта {currency} не поддерживается'
        
        current_limit = self.get_difference()
        current_currency = self.currencies[currency]

        if current_limit == 0:
            return f'Денег нет, держись'

        if currency in self.currencies:
            current_limit = current_limit / current_currency[0]

        if current_limit > 0:
            return (f'На сегодня осталось '
            f'{current_limit:.2f} {current_currency[1]}')

        abs_current_limit = abs(current_limit)

        return (f'Денег нет, держись: твой долг - '
            f'{abs_current_limit:.2f} {current_currency[1]}')
        

class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

        else:
            self.date = date=dt.datetime.now().date()
    