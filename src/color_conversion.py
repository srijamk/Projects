import sys

class ColorConversion:
  def cmyk_conversion(self, r, g, b):
    cmyk_list = []
    if r == 0 and g == 0 and b == 0:
      cmyk_list = [0, 0, 0, 1]
      return cmyk_list
    else:
      w = max(float(r) / 255, float(g) / 255, float(b) / 255)
      c = (float(w) - (float(r) / float(255))) / float(w)
      m = (float(w) - (float(g) / 255)) / float(w)
      y = (float(w) - (float(b) / 255)) / float(w)
      k = 1 - float(w)
      cmyk_list = [float(c), float(m), float(y), float(k)]
      return cmyk_list

if __name__ == '__main__':
  if len(sys.argv) != 4:
    r, g, b = raw_input("Enter three values respectively - Red, Green, Blue: ").split( )
  else:
    r = sys.argv[1]
    g = sys.argv[2]
    b = sys.argv[3]

  rgb = ColorConversion()
  print rgb.cmyk_conversion(int(r), int(g), int(b))
