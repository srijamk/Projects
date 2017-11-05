/*
 * Lesson 20  - Unit 2 - Technique - flag variables 
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;
import java.lang.Integer;

/*
class t1_lesson20_template{

     public static void main (String str[]) throws IOException {
          Scanner scan = new Scanner(System.in);
          
          System.out.println ("What number are we looking for?");
          int target = scan.nextInt();
          
          int x = 0;
          int flag = 0;
          
          while ( x != -1)
          {
               System.out.println ("Enter -1 to stop");
               x = scan.nextInt();
               
               if (x == target)
                    flag = 1;
          }
                              
          if (flag == 1)
                System.out.println (target + " was found");
          else
                 System.out.println (target + " was NOT found");
                              
     }

}

// Problem 1: What is output when a = 55 and b = 45?
class problem_one{
     public static void main (String str[]) throws IOException {
       int f = 0;
       int d = 2;
       while ( d <= a) {
         if ( a % d == 0 && b % d == 0)
           f = 1;
         d++;
       }
       System.out.println(f);

// Answer: 1
     }



// Problem 2: What is output when a = 66 and b = 25?
class problem_one{
     public static void main (String str[]) throws IOException {
       int f = 0;
       int d = 2;
       while ( d <= a) {
         if ( a % d == 0 && b % d == 0)
           f = 1;
         d++;
       }
       System.out.println(f);
     }

// Answer: 0

*/
// Coding Activity


import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;
import java.lang.Integer;

class Lesson_20_Activity {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        
        double farthest_north = -90.0;
        double farthest_south = 90.0;
        double farthest_east = -180.0;
        double farthest_west = 180.0;
        double another_location = 1.0;
        
        while (another_location != 0.0) {

          System.out.println("Please enter the latitude: ");
          double latitude = scan.nextDouble();

          System.out.println("Please enter the longitude: ");
          double longitude = scan.nextDouble();

          if (latitude >= 90 || latitude <= -90 || longitude > 180 || longitude < -180) {
              System.out.println("Incorrect Latitude or Longitude");
              
          } else {
              if (farthest_north == -90.0) {
                  farthest_north = latitude;
                  farthest_south = latitude;
              }
              else if (latitude > farthest_north) {
                  farthest_north = latitude;
              }
              else if (latitude < farthest_south) {
                  farthest_south = latitude;
              }
              
              if (farthest_east == -180.0) {
                  farthest_east = longitude;
                  farthest_west = longitude;
              }              
              if (longitude > farthest_east) {
                  farthest_east = longitude;
              }
              else if (longitude < farthest_west) {
                  farthest_west = longitude;
              }      
              
              System.out.println("Would you like to enter another location? ");
              another_location = scan.nextDouble();
          }
        System.out.println("Farthest North: " + farthest_north);
        System.out.println("Farthest South: " + farthest_south);
        System.out.println("Farthest East: " + farthest_east);
        System.out.println("Farthest West: " + farthest_west);
        }    
        System.out.println("Farthest North: " + farthest_north);
        System.out.println("Farthest South: " + farthest_south);
        System.out.println("Farthest East: " + farthest_east);
        System.out.println("Farthest West: " + farthest_west);
    }
}



