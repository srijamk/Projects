from int_to_ord import Convert
class Christmas():
    SECOND_SENTENCE = "my true love sent to me:"
    LAST_SENTENCE = "A partridge in a pear tree."
    # A dictionary's values are not in order when printed out; in this case, it was in the complete reverse
    gifts = ["Twelve drummers drumming", "Eleven pipers piping", "Ten lords a leaping", "Nine ladies dancing", "Eight maids a milking", "Seven swans a swimming", "Six geese a laying", "Five golden rings", "Four calling birds", "Three French hens", "Two turtle doves"]
    def get_verse(self, num_verse):

        # prints first sentence
        print "On the %s day of Christmas" % Convert().get_ord(num_verse)

        # prints constant sentence
        print self.SECOND_SENTENCE

        # for every number that applies to the given verse, print its corresponding sentence
        # ex: input --> 12, output --> every sentence from "12 drummers" to "2 turtle doves"
        for x in range(abs(num_verse - 12), 11):
            print self.gifts[x]

        # if the verse given is not the first verse, return the following last phrase
        if num_verse != 1:
            print "And a partridge in a pear tree. "

        # if not so, print the immutable last sentence
        else:
            print self.LAST_SENTENCE

GivenInteger = Convert()
number = int(input("Enter a number: "))
GivenNumVerse = Christmas()
print GivenNumVerse.get_verse(number)
