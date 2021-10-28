

def is_leap_year(leap_year):
  if leap_year % 4 == 0 and leap_year % 100 != 0:
    return True
  elif leap_year % 400 == 0:
    return True
  return False


def days_in_month(days_month, days_year):
  thirty_days = [4, 6, 9, 11]

  if days_month == 2:
    if is_leap_year(days_year):
      return 29
    else:
      return 28

  if days_month in thirty_days:
    return 30

  return 31


def day_of_week(day_month, day_year):
  t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  if day_month < 3:
    day_year -= 1
  return (day_year + int(day_year/4) - int(day_year/100) + int(day_year/400) + t[day_month - 1] + 1) % 7


def print_month_calendar(month, year):
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  month_year_title = f'{months[month - 1]} {year}'
  current_day_of_week = 0

  days = days_in_month(month, year)
  start_day_of_week = day_of_week(month, year)

  print(f'\n{month_year_title:^32}\n')
  print("   S   M   T   W   T   F   S\n")
  print('    ' * start_day_of_week, end = '')

  for day in range(1, days + 1):
    print(f'{day:>4}',end = '')
    if (day + start_day_of_week) % 7 == 0:
      print('\n')

  print()


def calendar_input():
  month = int(input("\nEnter a month number (1-12): "))
  year = int(input("Enter a year number after 1970: "))
  
  calendar = print_month_calendar(month, year)

  return calendar


def calendar_start():
  attempts = int(input("How many times would you like to build your calendar?: "))
  
  while attempts > 0:
    attempts -= 1
    calendar_input()