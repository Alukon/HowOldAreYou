from datetime import date

def calculate_age(born):
	today = date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

year_born = int(input('Введите год рождения: '))
month_born = int(input('Введите месяц рождения: '))
day_born = int(input('Введите день рождения: '))

print(calculate_age(date(year_born, month_born, day_born)))