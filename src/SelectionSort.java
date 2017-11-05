import java.util.Scanner;
import java.util.ArrayList;
class SelectionSort {
    public static void selectionSort () {
        ArrayList <Integer> list = reader();
        int count = 0;
        while (count < list.size() - 1) {
            System.out.println("Swapping " + list.get(count) + " with " + list.get(findMin(list, count + 1)) + " and count = " + count);
            swap(list, count, findMin(list, count + 1));
            System.out.print("Pass " + (count + 1) + ": ");
            for (int i = 0; i < list.size(); i++) {
                 System.out.print(list.get(i) + " ");
            }
            System.out.println();
            count++;
        }
    }
    public static void swap (ArrayList <Integer> list, int a, int b) {
        int temp = list.get(b);
        list.set(b, list.get(a));
        list.set(a, temp);
    }
    public static int findMin (ArrayList <Integer> list, int a) {
        int min = Integer.MAX_VALUE;
        for (int i = a; i < list.size(); i++) {
            if (list.get(i) < min) {
                min = i;
            }
        }
        System.out.print(min);
        return min;
    }
    public static ArrayList <Integer> reader () {
        Scanner scan = new Scanner (System.in);
        ArrayList <Integer> list = new ArrayList <Integer> ();
        int input = scan.nextInt();
        while (input != -1) {
            System.out.println("Enter a number to add to the list. Enter -1 to stop.");
            if (input != -1) {
                list.add(input);
                input = scan.nextInt();
            } else {
                break;
            }
        }
        return list;
    }
    public static void main (String [] args) {
        selectionSort();
    }
}