class Main {
    public static void main (String [] args) {
        Person p1 = new Person("Srija", 1000000);
        Person p2 = new Person("Hello Kitty", -5);
        System.out.println(Person.salary_sum(3, 5));
        System.out.println(Person.salary_sum(p1, p2));
        
        System.out.println(p1.get_salary());
        
    }
}