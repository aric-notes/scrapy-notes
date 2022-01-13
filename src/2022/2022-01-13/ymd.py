years = range(2022, 2026)
months = range(1, 13)


# get days in month
def get_days(year, month):
  tail = 32
  if month == 2 and year % 4 == 0: tail = 30
  if month == 2 and year % 4 != 0: tail = 29
  if month in [4, 6, 9, 11]: tail = 31
  return range(1, tail)

  # content of test_class.py
