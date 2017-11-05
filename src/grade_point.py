import math

class GradePoint():
    letter_grades = {
     "A+":4.5, "A": 4.0, "A-": 3.7,
    "B+":3.3, "B": 3.0, "B-": 2.7,
     "C+":2.3, "C": 2.0, "C-": 1.7,
     "D+": 1.3, "D": 1.0, "F": 0.0
    }

    def get_grade_point(self, letter_grade):
        # IF INPUT IS A LETTER GRADE
        if letter_grade in self.letter_grades:
            return self.letter_grades[letter_grade]
        # IF INPUT IS A FLOAT
        if float(letter_grade) in self.letter_grades.values():
            for key in self.letter_grades.keys():
                if self.letter_grades[key] == float(letter_grade):
                    return key
        # IF INPUT IS A FLOAT BUT IS NOT IN THE LIST OF VALUES
        if float(letter_grade) not in self.letter_grades.values():
            values = self.letter_grades.values()
            distances = []
            for value in values:
                distances.append(round(abs(float(value) - float(letter_grade)), 2))
            minimum = min(distances)
            return self.letter_grades.keys()[distances.index(minimum)]

    def get_key(self, value):
        for key in self.letter_grades.keys():
            if self.letter_grades[key] == value:
                return key

if __name__ == '__main__':
    givenLetterGrade = GradePoint()
    letter_grade = str(raw_input("Enter a letter grade: "))
    print givenLetterGrade.get_grade_point(letter_grade)
