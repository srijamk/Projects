import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;

class are_anagrams {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        System.out.println("Let's play Mad Libs. Enter a name. ");
        System.out.println("Enter a string: ");
        String first_name = scan.nextLine();
        System.out.println("Enter another name: ");
        String second_name = scan.nextLine();
        System.out.println(first_name + " gave " + second_name + ".");
    }
}