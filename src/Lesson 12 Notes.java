/*
 * Lesson 12 - Unit 2 - If's Making Decisions
 */

import java.util.Scanner;

class Lesson_12_Activity_Four {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        
        System.out.println("What is the temperature? ");
        int score = scan.nextInt();
        if (score <= 99)
          System.out.println("WARNING");
        if (score >= 102)
          System.out.println("WARNING");
        
    }
}