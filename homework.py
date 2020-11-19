import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        present_day = dt.datetime.now().date()
        day_stats = []
        for record in self.records:
            if record.date == present_day:
                day_stats.append(record.amount)
        return sum(day_stats)
    
    def get_week_stats(self):
        present_day = dt.datetime.now().date()
        delta = dt.timedelta(days=7)
        week_stats = 0
        first_date = present_day - delta
        for record in self.records:
            if first_date < record.date <= present_day:
                week_stats += record.amount
        return week_stats

    def difference(self):
        subtraction = self.limit - self.get_today_stats()
        return subtraction
        

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            return (f'Сегодня можно съесть что-нибудь ещё, ' 
                f'но с общей калорийностью не более {Calculator.difference(self)} кКал')

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
        try: 
            current_limit = Calculator.difference(self)
            current_currency = self.currencies[currency]
          
            if current_limit == 0:
                return f'Денег нет, держись'

            if currency in self.currencies.keys():
                current_limit = current_limit / current_currency[0]

            if current_limit > 0:
                return f'На сегодня осталось {current_limit:.2f} {current_currency[1]}'

            return f'Денег нет, держись: твой долг - {abs(current_limit):.2f} {current_currency[1]}'
    
        except KeyError:
            return f'Валюта {currency} не поддерживается'
        

class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

        else:
            self.date = date=dt.datetime.now().date()
    