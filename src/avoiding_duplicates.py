class Duplicates():
    def remove_duplicates(self, lst):
        return_list = []
        for item in lst:
            if item not in return_list:
                return_list.append(item)
        return return_list

if __name__ == '__main__':
    element = raw_input("Press Enter to continue: ")
    element_list = []
    if element == "":
        while element != "0":
            element = raw_input("Enter a word or number: ")
            if element != "0":
                element_list.append(element)
            else:
                print Duplicates().remove_duplicates(element_list)
