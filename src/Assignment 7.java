import java.util.Scanner;
import java.io.*;
import java.lang.Math;
import java.lang.Integer;

class Main {
    public static int[] convertToBinary (int b) {
        int [] a = {1, 1, 1, 1, 1, 1, 1, 1};
        for (int i = 0; i < 8; i++) {
            if (b < (int) Math.pow(2, (7 - i))) {
                a[i] = 0;
            }
            b = b % (int) Math.pow(2, (7 - i));
        }
        return a;
    }
    public static int[] addBin (int a[], int b[]) {
        int [] sum = {0, 0, 0, 0, 0, 0, 0, 0};
        String result = "";
        for (int i = 0; i < sum.length; i++) {
            if (a[i] + b[i] == 2) {
                result += "10";
            } else {
                result += Integer.toString(a[i] + b[i]);
            }
        }

        if (result.length() > 8) {
            for (int i = result.length() - 8; i <= 8; i++) {
                sum[i - 1] = result.charAt(i) - 48;
            }
            System.out.println("Error: overflow");
        } else {
            for (int j = 0; j < 8; j++) {
                sum[j] = result.charAt(j) - 48;
            }
        }
        return sum;
    }
    public static void printBin (int b[]) {
        for (int i = 0; i < b.length; i++) {
            System.out.print(b[i] + " ");
        }
    }
    public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);
        System.out.println("Enter a base ten number between 0 and 255, inclusive.");
        int first_num = scan.nextInt();
        System.out.println("Enter a base ten number between 0 and 255, inclusive.");
        int second_num = scan.nextInt();   
        
        System.out.println("\nFirst binary number: ");
        printBin(convertToBinary(first_num));
        
        System.out.println("\n\nSecond binary number: ");
        printBin(convertToBinary(second_num));
        
        System.out.println("\n\nAdded: " );
        printBin(addBin(convertToBinary(first_num), convertToBinary(second_num)));
        
    }

}
  