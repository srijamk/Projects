import glob

class Names():
    def get_distinct_names(self):
        files = glob.glob('/Users/Kiran/Documents/Baby Names Data Set/*.txt')
        boy_names = set()
        girl_names = set()
        for file in files:
            with open(file, 'r') as f:
                for line in f.readlines():
                    if line.split(",")[1] == 'F':
                        girl_names.add(line.split(",")[0])
                    else:
                        boy_names.add(line.split(",")[0])

        print "Girl Names: \n"
        for name in girl_names:
            print name

        print "Boy Names: \n"
        for name in boy_names:
            print name


print Names().get_distinct_names()
