class ChineseZodiac():
    animals = {
    2000:"Dragon", 2001:"Snake", 2002:"Horse",
    2003:"Sheep", 2004:"Monkey", 2005:"Rooster",
    2006:"Dog", 2007:"Pig", 2008:"Rat", 2009:"Ox",
    2010:"Tiger", 2011:"Hare"
    }
    def get_animal(self, year):
        return self.animals[(year - 2000) % 12 + 2000]

year = int(input("Enter year: "))
givenYear = ChineseZodiac()
print givenYear.get_animal(year)
