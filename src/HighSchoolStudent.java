public class HighSchoolStudent extends Student {
    private double final_gpa;
    private int level;
    private int studentId = 1;
    private String firstName, lastName;
    static int id = 1;
    public HighSchoolStudent(String fName, String lName, int gLevel, double gpa) {
        super(fName, lName, gLevel);
        final_gpa = gpa;
        if (!(gpa >= 0 && gpa <= 5)) {
            final_gpa = 0;
        }
    }
    public String toString() {
        return super.toString() + "\n\tGPA: " + final_gpa;
    }
}