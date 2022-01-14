from ymd import get_days

def test2021():
  assert get_days(2021, 1) == range(1, 32)
  assert get_days(2021, 2) == range(1, 29)
