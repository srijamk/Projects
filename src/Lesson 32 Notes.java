/*
 * Lesson 32 - Unit 4 - Parameters
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;

class Lesson_32_Activity_Four{
     
    public static void realTime (int seconds) {
        int hours = seconds / 3600;
        int minutes = (seconds - (hours * 3600)) / 60;
        seconds = seconds - ((hours * 3600) + (minutes * 60));
        System.out.println("Hours: " + hours);
        System.out.println("Minutes: " + minutes);
        System.out.println("Seconds: " + seconds);
    }
     public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);
        int seconds = scan.nextInt();
        realTime(seconds);
     }

}

