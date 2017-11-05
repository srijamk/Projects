 /* 
 * Lesson 5 - Unit 1 - Number Calculations and Order of Operations
 */

import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class t1_lesson07_template{


     public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner(System.in);
        
        int x = scan.nextInt();
        int y = scan.nextInt();
        
        System.out.println("Division: " + (x / y) + "\tRemainder: " + (x % y));
        
     }

}