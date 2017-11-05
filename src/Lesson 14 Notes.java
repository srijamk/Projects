/*
 * Lesson 14 - Unit 2  - Boolean Conditions
 *  
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
/*
class t1_lesson14_template{

     public static void main (String str[]) throws IOException {

          Scanner scan = new Scanner (System.in);
          int value = scan.nextInt();
          
          if (!(value >= 45 && value <= 78))
          {
            System.out.println("NOT BETWEEN 45 AND 78");
          } else {
            System.out.println("BETWEEN 45 AND 78");
          }

     }

}
*/
class Lesson_14_Activity_Three {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        
        System.out.println("Please enter the first octet: ");
        int first_octet = scan.nextInt();
        System.out.println("Please enter the second octet: ");
        int second_octet = scan.nextInt();
        System.out.println("Please enter the third octet: ");
        int third_octet = scan.nextInt();
        System.out.println("Please enter the fourth octet: ");
        int fourth_octet = scan.nextInt();
        if (first_octet < 0 || first_octet > 255) {
            System.out.println("Octet 1 is incorrect");
        }
        if (second_octet < 0 || second_octet > 255) {
            System.out.println("Octet 2 is incorrect");
        }
        if (third_octet < 0 || third_octet > 255) {
            System.out.println("Octet 3 is incorrect");
        }    
        if (fourth_octet < 0 || fourth_octet > 255) {
            System.out.println("Octet 4 is incorrect");
        }
        else if ((first_octet >= 0 && first_octet <= 255) && (second_octet >= 0 && second_octet <= 255) && (third_octet >= 0 && third_octet <= 255) && (fourth_octet >= 0 && fourth_octet <= 255)) {
            System.out.println("IP Address: " + first_octet + "." + second_octet + "." + third_octet + "." + fourth_octet);
        }
    }
}
/*
 
TRUTH TABLE
 _________________
| A | B | !A || B |
| T | T |    T    |
| T | F |    F    |
| F | T |    T    |
| F | F |    T    |
 -----------------
 
 */