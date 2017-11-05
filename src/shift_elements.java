import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class Shift {
    public static void shift (int[]a, int shift_amount){
        int abs_shift_amount = shift_amount;
        if (abs_shift_amount < 0) {
            abs_shift_amount = 0 - abs_shift_amount;
        }
        for (int i = 0; i < abs_shift_amount; i++) {
            if(shift_amount < 0) {
                rotateLeft(a);
            } else {
                rotateRight(a);
            }
        }
    }
    public static void main (String [] args) {
        int [] a = {1, 2, 3, 4};
        shift(a, 2);
           
        for(int i = 0; i < a.length; i++) {
            
            System.out.print(a[i] + " ");
        }
    }
    
    public static void rotateLeft(int[] a) {
        int temp = a[0];
        for (int i = 0; i < a.length - 1; i++) {
        
            a[i] = a[i + 1];
        }
        a[a.length - 1] = temp;
    }
    
    public static void rotateRight(int[] a) {
        int temp = a[a.length - 1];
        for (int i = a.length - 1; i > 0; i--) {
        
            a[i] = a[i - 1];
        }
        a[0] = temp;
    }
}
