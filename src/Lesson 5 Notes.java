 /* 
 * Lesson 5 - Unit 1 - Number Calculations and Order of Operations
 */

import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class t1_lesson05_template{


     public static void main (String str[]) throws IOException {
       
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Please enter a decimal number:");
        double firstnum = scan.nextDouble();
        double sum = firstnum - (int) firstnum;
        System.out.println("Answer: " + (int) (sum * 100));
     }

}