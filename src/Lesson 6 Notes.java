 /* 
 * Lesson 5 - Unit 1 - Number Calculations and Order of Operations
 */

import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class t1_lesson06_template{


     public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Please enter two integers:");
        int firstnum = scan.nextInt();
        int secondnum = scan.nextInt();
        double average = (((double) firstnum + (double) secondnum) / 2.0);
        System.out.println("The average is: " + average);
     }

}