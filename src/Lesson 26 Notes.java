/*
* Lesson 26 - Unit 3 - Algorithms on Arrays
*/
import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;


class t1_lesson26_template{
  
     public static void main (String str[]) throws IOException {
          Scanner scan = new Scanner(System.in);
          int tests [] = new int[20];   
          
          //initialize to true
          for (int i = 0; i < tests.length; i++)
          {
               tests[i] = (int)(Math.random()*55)+45;
          }
          
          for (int i = 0; i < tests.length; i++)
          {
               System.out.print(tests[i] + " "  );
          }
          System.out.println("What should be inserted? ");
          int insert = scan.nextInt();
          System.out.println("Where?");
          int index = scan.nextInt();
          
          for (int i = index; i < tests.length; i++)
          {
               tests[i] = tests[i - 1];
          }
          tests[index] = insert;
          for (int i = 0; i < tests.length; i++)
          {
               System.out.print(tests[i] + " "  );
          }
     }

}