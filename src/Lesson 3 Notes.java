import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

class t1_lesson03_template{


     public static void main (String str[]) throws IOException {
          // Input requires spot in memory to hold the input value
        Scanner scan = new Scanner (System.in);
        System.out.println("Hi there. What is your name?");
        String name = scan.nextLine();
        System.out.println("What adjective describes you?");
        String adjective = scan.nextLine();
        System.out.println("My name is " + name + ". I am " + adjective + ".");

     }

}