class SidewaysTriangle:
    def sideways_triangle_two(self, num):
        init_num = 1
        rows = ""
        while init_num <= num:
            row = "*" * init_num
            row_with_newline = row + "\n"
            rows += row_with_newline
            init_num += 1
        return rows
        if init_num == num:
            while num > 0:
                row = "*" * num
                row_with_newline = row + "\n"
                rows += row_with_newline
                num -= 1
            return rows

#triangle = SidewaysTriangle()
#print(triangle.sideways_triangle_two(3))
