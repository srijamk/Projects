class LineOfBestFit():
    def get_line_of_best_fit(self, x_list, y_list):
        first_numerator = sum(x_list) * sum(y_list)
        number = len(x_list)
        multiplicative_sum = 0.0
        exponent_sum = 0.0
        x_whole_squared = sum(x_list) ** 2
        x_average = float(sum(x_list) / len(x_list))
        y_average = float(sum(y_list) / len(y_list))
        index = 0
        while index < len(x_list):
            multiplicative_sum += x_list[index] * y_list[index]
            exponent_sum += x_list[index] ** 2
            index += 1
        slope = (multiplicative_sum - (first_numerator / number)) / (exponent_sum - (x_whole_squared) / number)
        b = (y_average - (slope * x_average))
        return "y = %.2fx + %.2f" % (slope, b)



x_value = raw_input("Press Enter to continue: ")
y_value = ""
x_list = []
y_list = []
if x_value == "":
    while x_value != "no":
        x_value = raw_input("Enter an x value: ")
        y_value = raw_input("Enter a y value: ")
        if x_value != "no" and y_value != "no":
            x_list.append(float(x_value))
            y_list.append(float(y_value))

print LineOfBestFit().get_line_of_best_fit(x_list, y_list)
