class Median():
    def get_median(self, a, b, c):
        return a + b + c - min(a, b, c) - max(a, b, c)

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = int(input("Enter a last number: "))
GivenNumList = Median()
print GivenNumList.get_median(a, b, c)
