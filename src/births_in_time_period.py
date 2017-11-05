import glob

class Names():
    def get_names(self, first_year, last_year):
        files = glob.glob('/Users/Kiran/Documents/Baby Names Data Set/*.txt')
        girl_names = []
        boy_names = []

        current_year = first_year
        while current_year < last_year:
            female_frequency = 0
            male_frequency = 0
            with open(files[current_year - 1900], 'r') as f:
                for line in f.readlines():
                    line_parts = line.split(",")
                    gender = line_parts[1]
                    current_frequency = int(line_parts[2])
                    if gender == 'F' and female_frequency < current_frequency:
                        female_name = line_parts[0]
                        female_frequency = current_frequency
                    if gender == 'M' and male_frequency < current_frequency:
                        male_name = line_parts[0]
                        male_frequency = current_frequency
            boy_names.append(male_name)
            girl_names.append(female_name)
            current_year += 1

        return "Most popular boy name: %s\nMost popular girl name: %s" % (max(set(boy_names), key=boy_names.count), max(set(girl_names), key=girl_names.count))

print Names().get_names(1990, 2012)
