import java.util.ArrayList;
public class School {
    private ArrayList<Student> final_students;
    private ArrayList<Teacher> final_teachers;
    public School (ArrayList<Student> students, ArrayList<Teacher> teachers) {
        final_students = students;
        final_teachers = teachers;
    }
    public String getGradeLevel(int level) {
        String result = "";
        for (Student s: final_students) {
            if (s.getLevel() == 12) {
                result += (s + "\n");
            }
        }
        return result;
    }
    public String toString () {
        String result = "Faculty:";
        for (Teacher t: final_teachers) {
            result += "\n" + t;
        }
        result += "\n\nStudent Body:";
        for (Student s: final_students) {
            result += "\n" + s;
        }
        return result;
    }
}