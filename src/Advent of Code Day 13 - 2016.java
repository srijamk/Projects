import java.io.*;
import java.util.*;

class Day_13_Part_1 {
    public static String binary (int num) {
        String result = "";
        int bin[] = new int[40];
        int index = 0;
        if (num == 0 || num == 1) {
            return "" + num;
        }
        while (num > 0) {
            bin[index++] = num % 2;
            num /= 2;
        }
        for(int i = index-1;i >= 0;i--){
            result += bin[i];
        }
        return result;
    }
    
    public static String get_num (int favorite_number, int x, int y) {
        int weird_num = x*x + 3*x + 2*x*y + y + y*y + favorite_number;
        return binary(weird_num);
    }
    
    public static boolean is_open (String num) {
        int count = 0;
        for (int i = 0; i < num.length(); i++) {
            if (num.charAt(i) == '1') {
                count++;
            }
        }
        return count % 2 == 0;
    }
    
    
    public static void main (String [] args) {
        //System.out.println(binary(185976));
        for (int i = 0; i <= 31; i++) {
            System.out.print(i);
        }
        System.out.println();
        for (int i = 0; i < 60; i++) {
            for (int j = 0; j < 60; j++) {
                if (i == 39 && j == 31) {
                    System.out.print("O ");
                } 
                if (i == 1 && j == 1) {
                    System.out.print("O ");
                } else {
                    if (is_open(get_num(1358, j, i))) {
                        System.out.print(". ");
                    } else {
                        System.out.print("# ");
                    }                
                }
                
            }
            System.out.println();
        }
    }
}