import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)
        return self.records

    def get_today_stats(self):
        today_total = 0
        for i in self.records:
            if i.date == dt.datetime.now().date():
                today_total += i.amount
        return today_total

    present_day = dt.datetime.now().date()
    delta = dt.timedelta(days=7)
    
    def get_week_stats(self):
        week_stats = 0
        first_date = self.present_day - self.delta
        for r in self.records:
            if first_date < r.date <= self.present_day:
                week_stats += r.amount
        return week_stats
        

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        difference = self.limit - self.get_today_stats()
        if self.get_today_stats() < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё,' \
                f' но с общей калорийностью не более {difference} кКал'
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = float(70)
    EURO_RATE = float(80)
    def get_today_cash_remained(self, currency):
        today_spent = self.get_today_stats()
        if currency == "eur":
            if today_spent < self.limit:
                return f'На сегодня осталось ' \
                    f'{"%.2f" % (float(self.limit/self.EURO_RATE) - float(today_spent/self.EURO_RATE))} Euro'
            elif today_spent > self.limit:
                return f'Денег нет, держись: твой долг - ' \
                    f'{"%.2f" % (float(today_spent/self.EURO_RATE) - float(self.limit/self.EURO_RATE))} Euro'   
            else:
                return 'Денег нет, держись'
        elif currency == "usd":
            if today_spent < self.limit:
                return f'На сегодня осталось ' \
                    f'{"%.2f" % (float(self.limit/self.USD_RATE) - float(today_spent/self.USD_RATE))} USD'
            elif today_spent > self.limit:
                return f'Денег нет, держись: твой долг - ' \
                    f'{"%.2f" % (float(today_spent/self.USD_RATE) - self.limit/self.USD_RATE)} USD'
            else:
                return 'Денег нет, держись'
        elif currency == "rub":
            if today_spent < self.limit:
                return f'На сегодня осталось {"%.2f" % (self.limit - today_spent)} руб'
            elif today_spent > self.limit:
                return f'Денег нет, держись: твой долг - {"%.2f" % (today_spent - self.limit)} руб'    
            else:
                return 'Денег нет, держись'


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        self.date = date
        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
    


