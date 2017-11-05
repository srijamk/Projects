class Sublist:
    def is_sublist(self, larger, smaller):
        indices_list = []
        for item in smaller:
            if item in larger:
                indices_list.append(larger.index(item))
            else:
                return False

        index = 0
        while index < len(indices_list) - 1:
            if indices_list[index] + 1 == indices_list[index + 1]:
                return True
            else:
                return False
            index += 1
larger = list(raw_input("Enter a list: ").split(", "))
smaller = list(raw_input("Enter another list: ").split(", "))
print Sublist().is_sublist(larger, smaller)
