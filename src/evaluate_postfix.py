from infix_to_postfix import Infix
class Postfix():
    def evaluate_postfix(self, string):
        postfix_expression = (Infix().infix_to_postfix(string)).split(" ")
        for token in postfix_expression:
            if token == '':
                postfix_expression.remove(token)
        values = []
        operators = []
        for token in postfix_expression:
            if token.isdigit():
                values.append(int(token))
            else:
                operators.append(token)

        index = 0
        operator_index = 0
        while index < len(values) and operator_index < len(operators):
            final_value = eval(str(values[0]) + operators[operator_index] + str(values[1]))
            values.pop(index)
            values[0] = final_value
            index += 1
            operator_index += 1

        return final_value

string = raw_input("Enter a string: ")
print Postfix().evaluate_postfix(string)
