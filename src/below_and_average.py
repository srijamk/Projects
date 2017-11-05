class BelowAndAverage():
    def get_below_and_average(self, number_list):
        for number in number_list:
            number = int(number)
        average = sum(number_list) / len(number_list)
        below_average_list = []
        average_list = []
        above_average_list = []
        for item in number_list:
            if item > average:
                above_average_list.append(int(item))
            elif item < average:
                below_average_list.append(int(item))
            else:
                average_list.append(int(item))
        return "Above average: " + str(above_average_list) + "\n" + "Below average: " + str(below_average_list) + "\n" + "Average: " + str(average_list)

print BelowAndAverage().get_below_and_average(number_list)
