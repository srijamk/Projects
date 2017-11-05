import sys

class ReadFile():
  def write_file(self, file):
    file = open("out.txt", "w")
    with open(str(file)) as f:
      for line in f:
        file.write(str(line) + "\n")
