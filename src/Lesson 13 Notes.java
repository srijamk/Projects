import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

class t1_lesson13_template{

     public static void main (String str[]) throws IOException {

       Scanner scan = new Scanner(System.in);
       
       System.out.println("Please enter your age: ");
       int age = scan.nextInt();
       
       if(age >= 18) {  
         System.out.println("You can vote.");
         
       } else {
         System.out.println("You can't vote.");  
       }
     
     }

}