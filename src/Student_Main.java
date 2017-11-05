class Student_Main {
    public static void main (String [] args) {
        // Student objects
        Student s = new Student("Buzz Lightyear", new int [] {90, 94, 99}, "None");
        Student u = new UnderGrad("Nemo", new int [] {90, 90, 100}, "None");
        Student g = new GradStudent("Wall-E", new int [] {85, 70, 90}, "None", 1234);
        
        // Test setGrade
        s.setGrade("A");
        g.setGrade("A");
        u.setGrade("A");
        //System.out.println(u.getGrade());
        
        // Test getID
        /*
        System.out.println(u.getID());
        System.out.println(g.getID());
        System.out.println(s.getID());
        */
        
        // Test computeGrade
        s.computeGrade();
        u.computeGrade();
        g.computeGrade();
        
        // Test getGrade
        System.out.println(s.getGrade());
        System.out.println(u.getGrade());
        System.out.println(g.getGrade());
        
        // Test Downcasting
        Student s1 = new GradStudent();
        GradStudent g1 = new GradStudent();
        Student u1 = new UnderGrad();
        int x = g1.getID();
        int y = g1.getID();
        System.out.println(x);
        //System.out.println((String) u1);
        
        // Test Abstract
        Beverage c = new Coffee(3);
        Beverage t = new Tea(3);
        c.Make();
        System.out.println();
        t.Make();
        System.out.println();
        
        // Test Interface
        IAmAFather h = new FamilyPerson();
        ((IAmAProgrammer) h).DoProgramming();
        h.TeachKids();
        
        IAmAProgrammer p = new Programmer();
        ((IAmAFather) p).DoProgramming();
        
    }
}