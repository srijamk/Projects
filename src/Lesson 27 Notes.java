/*
* Lesson 27 - Unit 3 - Algorithms - searching
*/
import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;


class t1_lesson27_template{

  
     public static void main (String str[]) throws IOException {
          Scanner scan = new Scanner (System.in);
          
          double list [] =  {2.3 , 4.7 , 5.25 , 9.5 , 2.0 , 1.2 , 7.129 , 5.4 , 9.4 };
          
          System.out.println( "What are you looking for? ");
          double look = scan.nextDouble();
          int is_found = 0;
          //search for value in the array, print -1 if not found
          for (int i = 0; i < list.length; i++) {
            if (look == list[i]) {
              is_found = 1;
            }
          }
          if (is_found == 1) {
            System.out.println(look + " was found.");
          } else {
            System.out.println(-1);
          }
     
     }
}