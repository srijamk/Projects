import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;
import java.util.Arrays;

class Main {
    public static void main (String [] args) {
        Scanner scan = new Scanner (System.in);
        int [] first_array = new int[10000];
        
        System.out.println("Enter the values for the first array, up to 10000 values, enter a negative number to quit");
        int element = scan.nextInt();
        int counter = 0;
        int is_valid = 0;
        while (element >= 0) {
            first_array[counter] = element;
            if (counter != 0 && first_array[counter - 1] > element) {
                is_valid = 1;
            }
            element = scan.nextInt();
            counter ++;
        }
        
        System.out.println("First Array: ");
        for (int i = 0; i < counter; i++) {
            System.out.print(first_array[i] + " ");
        }

        
        int [] second_array = new int[10000];
        System.out.println("\nEnter the values for the second array, up to 10000 values, enter a negative number to quit");
        int second_element = scan.nextInt();
        int second_counter = 0;
        int second_is_valid = 0;
        while (second_element >= 0) {
            second_array[second_counter] = second_element;
            if (second_counter != 0 && second_array[second_counter - 1] > second_element) {
                second_is_valid = 1;
            }
            
           
            second_element = scan.nextInt();
            second_counter ++;
        }
        System.out.println("\n\nSecond Array: ");
        for (int i = 0; i < second_counter; i++) {
            System.out.print(second_array[i] + " ");
        }
        if ((is_valid == 1) || (second_is_valid == 1)) {
            System.out.println("\n\nERROR: Array not in correct order");
        } else {
        int [] merged_array = new int[counter + second_counter];
        for (int i = 0; i < counter; i++) {
            merged_array[i] = first_array[i];
        }
        for (int j = 0; j < second_counter; j++) {
            merged_array[counter + j] = second_array[j];
        }
        System.out.println("\n\nMerged Array: ");
        java.util.Arrays.sort(merged_array);
        for (int i = 0; i < counter + second_counter; i++) {
            System.out.print(merged_array[i] + " ");
        }
        }
    }
}
