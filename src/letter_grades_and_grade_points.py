from grade_point import GradePoint

user_input = raw_input("Enter a letter grade or grade point: ")
while user_input != "":
    print GradePoint().get_grade_point(user_input)
    user_input = raw_input("Enter a letter grade or grade point: ")
