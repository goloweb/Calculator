import datetime as dt

date_format = '%d.%m.%Y'

moment = dt.datetime.strptime('16.12.2022', date_format)

day = '11.04.2022'


class Calculator():
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    now = dt.datetime.now()
    today = now.date()
    today_sum = 0
    margin = 0

    def add_record(self, examp):
        self.records.append(examp)

    def get_today_status(self):
        self.today_sum = 0
        for rec in self.records:
            if rec.date == self.today:
                self.today_sum += rec.amount

    def get_reminded(self):
        self.margin = self.limit - self.today_sum

    def get_week_status():
        pass


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    USD_RATE = 74.85
    EURO_RATE = 81.71

    def get_today_cash_status(self):
        print(f'Сегодня вы потратили {self.today_sum} рублей')

    def get_today_cash_remained(self, currency):
        self.get_reminded()
        self.currency = currency
        print(f'limit: {self.limit}, margin: {self.margin}')
        if self.margin > 0:
            if self.currency == 'rub':
                print(f'Сегодня можно потратить еще: {self.margin} рублей')
            elif self.currency == 'usd':
                self.margin = round(self.margin / self.USD_RATE, 2)
                print(f'Сегодня можно потратить еще: {self.margin} долларов')
            elif self.currency == 'eur':
                self.margin = round(self.margin / self.EURO_RATE, 2)
                print(f'Сегодня можно потратить еще: {self.margin} евро')
            else:
                print('Вы ввели название валюты неверно')
        elif self.margin < 0:
            if self.currency == 'rub':
                self.margin = self.margin * -1
                print(
                    f'На сегодня лимит изчерпан. Ваш долг: {self.margin} рублей')
            elif self.currency == 'usd':
                self.margin = round(self.margin / self.USD_RATE * -1, 2)
                print(
                    f'На сегодня лимит изчерпан. Ваш долг: {self.margin} долларов')
            elif self.currency == 'eur':
                self.margin = round(self.margin / self.EURO_RATE * -1, 2)
                print(
                    f'На сегодня лимит изчерпан. Ваш долг: {self.margin} евро')
            else:
                print('Вы ввели название валюты неверно')
        else:
            print('Вы потратили все до копейки')

    def show(self):
        print(self.margin)


class Record():
    def __init__(self, amount, comment, date=day):
        date_format = '%d.%m.%Y'
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, date_format).date()

    def show(self):
        print(self.date)


fir = CashCalculator(150)

r1 = Record(125, 'Тренажерка')
r2 = Record(135, 'Тренажерка')
r3 = Record(145, 'Тренажерка')

r4 = Record(120, 'Тренажерка')
r5 = Record(600, 'Тренажерка')
r6 = Record(1000, 'Тренажерка', '03.04.2022')

fir.add_record(r1)
fir.add_record(r2)
fir.add_record(r3)

fir2 = CaloriesCalculator(1000)
fir2.add_record(r4)
fir2.add_record(r5)
fir2.add_record(r6)

r1.show()

fir.get_today_status()

fir2.get_today_status()

fir3 = CashCalculator(720)

fir3.add_record(r4)
fir3.add_record(r5)
fir3.add_record(r6)

# fir3.get_today_status()

fir3.get_today_cash_remained('usd')

fir3.get_today_cash_status()
