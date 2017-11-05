import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.lang.Math;
/*
class Lesson_35_Notes {
    public static int max (int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }   
    
    public static int max(int a, int b, int c) {
        return max(max(a, b), c);
    }
    
    public static void main (String[] args) {
        Scanner scan = new Scanner (System.in);
        
        System.out.println("Enter three integers: ");
        int x = scan.nextInt();
        int y = scan.nextInt();
        int z = scan.nextInt();
        System.out.println("Max of " + x + " and " + y + " = " + max(x, y));
        System.out.println("Max of " + x + ", " + y + ", and " + z + " = " + max(x, y, z));
    }
}
*/
class Lesson_35_Activity {
    public static int randomize (int a, int b) {
        return (int) (Math.random() * Math.abs(a - b) + Math.min(a, b));
    }
    
    public static int randomize (int a) {
        return (int) (Math.random() * a);
    }
    
    public static double randomize (double a, double b) {
        return Math.random() * Math.abs(a - b) + Math.min(a, b);
    }
    
    public static double randomize (double a) {
        return Math.random() * a;
    }
}