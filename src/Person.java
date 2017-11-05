public class Person {
    private String name;
    private int salary;
    private static int ppl_count;
    Person (String name, int salary) {
        this.name = name;
        this.salary = salary;
        ppl_count++;
    }
    public String get_name () {
        return name;
    }
    public static int ppl_count () {
        return ppl_count;
    }
    public static int salary_sum (int a, int b) {
        a = 0;
        return a + b;
    }
    public static int salary_sum (Person a1, Person a2) {
        
        int sum = a1.get_salary() + a2.get_salary();
        a1 = null;
        return sum;
    }
    public int get_salary () {
        return this.salary;
    }
    
}
