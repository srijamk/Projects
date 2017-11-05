/*
 * Lesson 24 - Unit 3 - The For Loop  
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;

class t1_lesson24_template{

     public static void main (String str[]) throws IOException {
          String list [] = {"li", "fe ", "is ", "go", "od", ":)"};   
          String list2[] = new String [10];
          for (int i = 20; i <= 100; i += 2) {
               System.out.println(i/2 + " x 2 = " + i + " ");
          }
          System.out.println();
          for (int i = 0; i < list.length; i++) {
               System.out.print(list[i]);
          }
          
          System.out.println();
          for (int n = 0; n < list.length; n++) {
            list2[n] = list[n]; 
            System.out.println(list2[n]);
          }
     }

}

class Lesson_24_Activity_One {
    public static void main(String[] args) {
      for (int num = 23; num <= 89; num++) {
        if (num == 32 || num == 42 || num == 52 || num == 62 || num == 72 || num == 82) {
          System.out.print(num + "\n");
        } else {
          System.out.print(num + " ");
        }
      }
    }
}

class Lesson_24_Activity_Two {
    public static void main(String[] args) {
      Scanner scan = new Scanner (System.in);
      System.out.println("Enter a number between 0 and 100: ");
      int number = scan.nextInt();
      if (0 <= number && number <= 100) {
        for (int num = number; num <= 100; num++) {
          if (num - number == 19 || num - number == 39 || num - number == 59 || num - number == 79 || num - number == 99) {
            System.out.print(num + "\n"); 
          } else {
            System.out.print(num + " ");
          }
          
        }          
      } else {
        System.out.println("error");
      }

    }
}