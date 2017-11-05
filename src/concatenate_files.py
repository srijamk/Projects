import os.path
class File():
    def concatenate_files(self, file):
        for f in file:
            read_f = open(f, 'r')
            print read_f.read()

files = raw_input("Enter a file name: ").split(", ")
len_lst = len(list(files))
for file in list(files):
    if os.path.isfile(file) == False:
        list(files).pop(list(files).index(file))

if len(list(files)) == len_lst:
    print File().concatenate_files(list(files))
else:
    print "One of your files is invalid. "
