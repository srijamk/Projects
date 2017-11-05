/*
 * Lesson 9 - Unit 1 - Math functions. 
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

import java.lang.Math;

class t1_lesson09_template{

     public static void main (String str[]) throws IOException {

       
            Scanner scan = new Scanner (System.in);
          
            System.out.println("Please enter 1 int: ");
            int x = scan.nextInt();
            
            System.out.println("Please enter 1 double: ");
            double a = scan.nextDouble();
            
            System.out.println("Answers: ");
            /*
            // Math Module
            System.out.println(Math.pow(x, a));
            System.out.println(Math.abs(x - a));
            System.out.println(Math.sqrt(x));
            */
            System.out.println((int)(Math.random() * 41) +-205);
               
          
          

     }

}


