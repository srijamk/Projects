import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
class Main {
  
    public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);
        
        // Test Grades
        System.out.print("Please enter your test grades. \nTest 1: ");
        double first_test = scan.nextDouble();
        System.out.print("Test 2: ");
        double second_test = scan.nextDouble();
        double test_average = ((first_test + second_test) / 2.0);
          
        // Quiz Grades
        System.out.println("\nPlease enter your quiz grades. \nQuiz 1: ");
        double first_quiz = scan.nextDouble();
        System.out.print("Quiz 2: ");
        double second_quiz = scan.nextDouble();   
        System.out.print("\nQuiz 3:");
        double third_quiz = scan.nextDouble();
        double quiz_average = ((first_quiz + second_quiz + third_quiz) / 3.0);
          
        // Homework Grade
        System.out.print("\nPlease enter your homework average. \nHomework: ");
        double homework = scan.nextDouble();
        
        // Final Averages
        System.out.print("\nTest Average: " + test_average + "\n");
        System.out.println("Quiz Average: " + quiz_average + "\n");
        System.out.println("Final Grade: " + ((test_average * 0.5) + (quiz_average * 0.3) + (homework * 0.2)));
        
    }
}