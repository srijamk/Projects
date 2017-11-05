'''
The baby names data set consists of over 200 files. Each file contains a list of 100
names, along with the number of times each name was used. There are two files for
each year: one containing names used for girls and the other containing names used
for boys. The data set includes data for every year from 1900 to 2012.
Write a program that reads every file in the data set and identifies all of the names
that were most popular in at least one year. Your program should output two lists:
one containing the most popular names for boys and the other containing the most
popular names for girls. Neither of your lists should include any repeated values.
'''

import glob

class Names():
    def get_top_baby_names(self, year):
        # Gets list of files (with extension txt) from a directory
        files = glob.glob('/Users/Kiran/Documents/Baby Names Data Set/*.txt')
        #print len(files)
        female_name_set = set()
        male_name_set = set()
        for file in files[year-1900:year-1899]:
            male_frequency = 0
            female_frequency = 0
            male_name = ''
            female_name = ''
            with open(file, 'r') as f:
                for line in f.readlines():
                    line_parts = line.split(",")
                    gender = line_parts[1]
                    current_frequency = int(line_parts[2])
                    if gender == 'M' and male_frequency < current_frequency:
                        male_name = line_parts[0]
                        male_frequency = current_frequency

                    elif gender == 'F' and female_frequency < current_frequency:
                        female_name = line_parts[0]
                        female_frequency = current_frequency
            female_name_set.add(female_name)
            male_name_set.add(male_name)
        print female_name_set, male_name_set

print Names().get_top_baby_names()
