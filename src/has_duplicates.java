import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class Duplicates {
    public static boolean has_duplicates (int a[]) {
        for (int i = 0; i < a.length; i++) {
            int counter = 0;
            for (int j = 0; j < a.length; j++) {
                if (a[i] == a[j]) {
                    counter++;
                }
            }
            if (counter >= 2) {
                return true;
            }
        }
        return false;
    }
    
    public static void main (String [] args) {
        int [] array = {1, 2, 3, 4, 5};
        int [] second_array = {1, 1, 2, 3};
        System.out.println(has_duplicates(array));
        System.out.println(has_duplicates(second_array));
    }
}