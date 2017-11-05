import java.util.Scanner;
import java.lang.Math; 

class Lesson_17_Activity_One {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);

        System.out.println("Enter two numbers: ");
        int first_num = scan.nextInt();
        int second_num = scan.nextInt();        

    if (first_num % 2 == 1) {
      while (first_num < second_num) {
        System.out.print(first_num + 1 + " ");
        first_num += 2;
      }
    } else {
        while (first_num <= second_num) {
          System.out.println(first_num);
          first_num += 2;
      }
    }
    
/*
 * Write your code here
 * Copy and paste your entire program to Code Runner
 * to complete the activity, from the first import statement
 * to the last bracket.
 */
     }
}