import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

class t1_lesson11_template{

     public static void main (String str[]) throws IOException {

       Scanner scan = new Scanner(System.in);

       System.out.println("Enter a decimal value: ");
       
       double value = scan.nextDouble();

       if (value == 17.25)
         System.out.println("It is a scooter");
        
     }

}