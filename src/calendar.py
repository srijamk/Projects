import sys

class Calendar:
  def day_of_the_week(self, m, d, y):
    y0 = y - (14 - m) / 12
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2
    d0 = (d + x + (31 * m0) / 12) % 7
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return day_list[d0]

cal = Calendar()
print cal.day_of_the_week(int(month), int(day), int(year))


if __name__ == '__main__':
  if len(sys.argv) != 4:
    month, day, year = raw_input("Enter three values respectively - Month, Day, Year: ").split(", ")
  else:
    month = sys.argv[1]
    day = sys.argv[2]
    year = sys.argv[3]

  cal = Calendar()
  print cal.day_of_the_week(int(month), int(day), int(year))
