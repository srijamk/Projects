
import java.io.*;
import static java.lang.System.*;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.lang.Math;
import java.util.ArrayList;

class Day_2 {
    /*
     * Advent of Code Day 2: Part 1
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_2.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_2.out")));
        int num = 5;
        for (int i = 0; i < 6; i++) {
            String line = f.readLine();
            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == 'L' && num != 1 && num != 4 && num != 7) {
                    num -= 1;
                } 
                if (line.charAt(j) == 'R' && num != 3 && num != 6 && num != 9) {
                    num += 1;
                }
                if (line.charAt(j) == 'U' && num != 1 && num != 2 && num != 3) {
                    num -= 3;
                }
                if (line.charAt(j) == 'D' && num != 7 && num != 8 && num != 9) {
                    num += 3;
                }
            }
            System.out.println(num);
        }
    }
    */
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_2.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_2.out")));
        int num = 5;
        // 'A' -> 65, 'B' -> 66, 'C' -> 67, 'D' -> 68
        for (int i = 0; i < 6; i++) {
            String line = f.readLine();
            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == 'L' && num != 1 && num != 2 && num != 5 && num != 65 && num != 68) {
                    num--;
                } 
                if (line.charAt(j) == 'R' && num != 1 && num != 4 && num != 9 && num != 67 && num != 68) {
                    num++;
                } 
                if (line.charAt(j) == 'U' && num == 65) {
                    num = 6;
                } else if (line.charAt(j) == 'U' && num == 66) {
                    num = 7;
                } else if (line.charAt(j) == 'U' && num == 67) {
                    num = 8;
                } else if (line.charAt(j) == 'U' && num == 68) {
                    num = 66;
                } else if (line.charAt(j) == 'U' && num == 3) {
                    num = 1;
                } else if (line.charAt(j) == 'U' && num != 1 && num != 2 && num != 5 && num != 4 && num != 9) {
                    num -= 4;
                } 
                if (line.charAt(j) == 'D' && num == 66) {
                    num = 68;
                } else if (line.charAt(j) == 'D' && num == 6) {
                    num = 65;
                } else if (line.charAt(j) == 'D' && num == 7) {
                    num = 66;
                } else if (line.charAt(j) == 'D' && num == 8) {
                    num = 67;
                } else if (line.charAt(j) == 'D' && num == 66) {
                    num = 68;
                } else if (line.charAt(j) == 'D' && num == 1) {
                    num = 3;
                } else if (line.charAt(j) == 'D' && num != 5 && num != 9 && num != 65 && num != 68 && num != 67) {
                    num += 4;
                } 
                
            }
            if ((char)num == 'A' || (char)num == 'B' || (char)num == 'C' || (char)num == 'D') {
                System.out.println((char)num);
            } else {
                System.out.println(num);
            }
            
        }
    }
}
