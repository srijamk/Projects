/*
 * Lesson 1011 Coding Activity 
 * 
 * Input a String to represent the octal number and translate to the base ten number. 
 * The octal number must be 8 digits or less. 
 * 
 * Your program should also check that all the digits are 0 - 7, then translate the 
 * number to base ten. 
 * 
 * Sample Run 1: 
 * Enter a number in base 8: 
 * 1287 
 * ERROR: Incorrect Octal Format 
 * 
 * Sample Run 2: 
 * Enter a number in base 8: 
 * 123 
 * 83 
 * 
 * Sample Run 3: 
 * Enter a number in base 8: 
 * 1111111111 
 * ERROR: Incorrect Octal Format
 *   
 */ 

import java.util.Scanner;
import java.lang.Math; 
import java.lang.Integer;
import java.lang.Character;
class Lesson_1011_Activity{
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        System.out.println("Enter a number in base 8: ");
        String base_8 = scan.nextLine();
        int invalid = 0;
        for (int i = 0; i < base_8.length(); i++) {
            if (! ((base_8.charAt(i) == '0') || (base_8.charAt(i) == '1') || (base_8.charAt(i) == '2') || (base_8.charAt(i) == '3') || (base_8.charAt(i) == '4') || (base_8.charAt(i) == '5') || (base_8.charAt(i) == '6') || (base_8.charAt(i) == '7'))) {
                invalid = 1;
            }
        }
        if (base_8.length() > 8) {
            invalid = 1;
        }
        if (invalid == 1) {
            System.out.println("ERROR: Incorrect Octal Format");
        } else {
            int sum = 0;
            for (int i = 0; i < base_8.length(); i++) {
                sum += Integer.parseInt(Character.toString(base_8.charAt(i))) * (Math.pow(8, (base_8.length() - 1 - i)));
            } 
            System.out.println(sum);
        }
    }
}



