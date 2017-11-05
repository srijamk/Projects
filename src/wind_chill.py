import sys
import math

class WindChill:
  def wind_chill(self, t, v):
    return round((35.74 + 0.6215 * float(t) + (0.4275 * t - 35.75) * math.pow(float(v), 0.16)), 3)

if __name__ == '__main__':
  if len(sys.argv) != 3:
    t, v = raw_input("Enter two numbers respectively - Temperature(Fahrenheit), (Wind Speed(mph): ").split( )
  else:
    t = sys.argv[1]
    v = sys.argv[2]

  wind = WindChill()
  print wind.wind_chill(float(t), float(v))
