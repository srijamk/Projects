import sys

class QuickSort():
	def sort(self, lst):
		smaller = []
		pivotList = []
		bigger = []
		if len(lst) <= 1:
			return lst
		else:
			pivot = lst[0]
			for i in lst:
				if i < pivot:
					smaller.append(i)
				elif i < pivot:
					bigger.append(i)
				else:
					pivotList.append(i)
				smaller = self.sort(smaller)
				bigger = self.sort(bigger)
		return smaller + pivotList + bigger

if __name__ == '__main__':
	if len(sys.argv) != 2:
		lst = raw_input("Enter a valid list of numbers: ").split(" ")
	else:
		lst = sys.argv[1]
	quick = QuickSort()
	print quick.sort(lst)
