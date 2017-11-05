import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class Sum {
    public static int arraySum (int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = sum + arr[i];
        }
        return sum;
    }
    
    public static void main (String [] args) {
        int [] arr = {1, 2, 3, 4, 5};
        System.out.println(arraySum(arr));
    }
}