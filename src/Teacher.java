public class Teacher extends Person {
    private String final_subject;
    public Teacher (String fName, String lName, String subject) {
        super(fName, lName);
        final_subject = subject;
    }
    public String toString() {
        return super.toString() + "\n\tSubject: " + final_subject;
    }
}