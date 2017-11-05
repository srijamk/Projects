import glob

class Names():
    def get_gender_neutral_names(self, year):
        all_names = []
        files = glob.glob('/Users/Kiran/Documents/Baby Names Data Set/*.txt')
        for file in files[(year - 1900):(year - 1899)]:
            with open(file, 'r') as f:
                for line in f:
                    line_parts = line.split(",")
                    all_names.append(line_parts[0])
        for name in all_names:
            if all_names.count(name) == 2:
                print name

print Names().get_gender_neutral_names(1950)
