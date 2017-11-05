/*
 * Lesson 10 - Unit 1 - Roundoff error. 
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

import java.lang.Math;

class t1_lesson10_template{

     public static void main (String str[]) throws IOException {

        Scanner scan = new Scanner (System.in);
        System.out.println("Please enter two decimal values: ");
        double firstnum = scan.nextDouble();
        double secondnum = scan.nextDouble();
        System.out.println(firstnum * 1000 - secondnum * 1000);
        
     }

}

