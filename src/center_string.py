class Terminal():
    def get_spaces(self, string, width):
        return ((width - len(string)) / 2) * " " + string

GivenString = Terminal()
width = 206
print GivenString.get_spaces("I Know Why the Caged Bird Sings", width)
#print GivenString.get_spaces("I know why the caged bird sings, ah me,", width)
#print GivenString.get_spaces("When his wing is bruised and his bosom sore,", width)
#print GivenString.get_spaces("When he beats his bars and would be free;", width)
#print GivenString.get_spaces("It is not a carol of joy or glee,", width)
#print GivenString.get_spaces("But a prayer that he sends from his heart's deep core,", width)
#print GivenString.get_spaces("But a plea, that upward to Heaven he flings -", width)
#print GivenString.get_spaces("I know why the caged bird sings.", width)
print GivenString.get_spaces("Y O U   C A N T   C E N T E R   M E", width) 
