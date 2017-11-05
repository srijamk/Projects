class OutputPatterns:
    def right_triangle(self, num):
        ### Takes a number and generates a pattern similar to the following:
        ### ****
        ### ***
        ### **
        ### *
        rows = ""
        while num > 0:

            row = "*" * num
            row_with_newline = row + "\n"
            rows += row_with_newline
            num -= 1
        return rows
