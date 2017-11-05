import sys

class WriteFile():
  def write_file(self, file):
    file1 = open("out.txt", "w")
    with open(str(file)) as f:
      for line in f:
        file1.write(str(line) + "\n")

if __name__ == '__main__':
  if len(sys.argv) != 2:
    file = raw_input("Enter a valid file: ")
  else:
    file = sys.argv[1]
  write = WriteFile()
  print write.write_file(file)
