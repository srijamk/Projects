/*
 * Lesson 19 - Unit 2 - More Loops
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;

class t1_lesson19_template{


     public static void main (String str[]) throws IOException {

          int a = 45;
          int b = 30;
          
          while ( b !=0 )
          {
               int r = a % b;
               a = b;
               b = r;
              
          }

          System.out.println(a);
                
            
     }

}

// Problem 1: What does the following loop do?

int num = scan.nextInt();
int sum = 0;

while ( num > 0) {
    sum += num % 10;
    num /= 10;
}
System.out.print(sum);

// num = 91
// sum = 0
// 1: sum = 1, num = 9
// 2: sum = 10, num = 0
// prints 10

// Answer: Sums the digits of num