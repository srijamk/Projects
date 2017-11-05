import java.io.*;
import java.util.*;

class Bubble {
    public static void printArr (int [] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
    public static void swap (int [] arr, int j, int k) {
        int temp = arr[k];
        arr[k] = arr[j];
        arr[j] = temp;    
    }
    public static boolean bubbleSort (int [] arr, int start) {
        if (start == 0) {
            printArr(arr);
            return true;
        }
        for (int j = 0; j < start - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
        bubbleSort(arr, start - 1);
        return true;
    }
    public static void main (String [] args) {
        int [] arr = {8, 3, 7, 10, 1, 3, 7, 1, 3, 9};
        long startTime = System.nanoTime();
        bubbleSort(arr, 10);
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);  //divide by 1000000 to get milliseconds.
        System.out.println(duration);
    }
}