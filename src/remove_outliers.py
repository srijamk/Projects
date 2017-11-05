class RemoveOutliers():
    def remove_outliers(self, lst):
        for x in range(2):
            lst.pop(lst.index(max(lst)))
            lst.pop(lst.index(min(lst)))
        return lst
number = raw_input("Press Enter to continue: ")
number_list = []
if number == "":
    while number != 0:
        number = int(raw_input("Enter a number: "))
        if number != 0:
            number_list.append(number)
        else:
            print RemoveOutliers().remove_outliers(number_list)
