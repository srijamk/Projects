import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.lang.Math;

class Lesson_36_Notes {
    public static int mystery (int n) {

        if (n == 1) {
            return 1;
        } else {
            return n * mystery(n - 1);
        }
    }
    public static void main (String[] args) {
        Scanner scan = new Scanner (System.in);
        
        int n = scan.nextInt();
        System.out.println(n + "! = " + mystery(n));
    }
}