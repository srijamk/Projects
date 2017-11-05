import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

class t1_lesson04_template{


     public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);     
        System.out.println("Hi there. What is your name?");
        String name = scan.nextLine();
        System.out.println("Hi " + name + ". How old are you?");
        int age = scan.nextInt();
        System.out.println(name + ", you will be 100 in " + (100 - age) + " years.");
     }

}