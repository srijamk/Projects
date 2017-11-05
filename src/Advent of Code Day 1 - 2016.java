 import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.lang.Math;
import java.util.ArrayList;

class Day_1_Part_1 {
    
    public static void main (String [] args) {
        String line = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1";
        String [] split_line = line.split(", ");
        int facing_dir = 0;
        // 0 - North, 1 - East, 2 - South, 3 - West
        int x_pos = 0;
        int y_pos = 0;
        ArrayList <String> list = new ArrayList <String>();
        for (int j = 0; j < 100; j++) {
            int change_amt = Integer.parseInt(split_line[j].substring(1));
            char dir = split_line[j].charAt(0);
            if (facing_dir < 3 && dir == 'R') {
                facing_dir++; 
            } else if (facing_dir == 3 && dir == 'R') {
                facing_dir = 0;
            } else if (facing_dir > 0 && dir == 'L') {
                facing_dir--;
            } else {
                facing_dir = 3;
            }
            
            
            if (facing_dir == 1) {
                for (int i = 1; i <= change_amt; i++) {
                    if (list.contains((x_pos + i) + "" + y_pos)) {
                        System.out.println("REPEAT: " + "(" + (x_pos + i) + ", " + y_pos + ")");
                    } else {
                        list.add("" + (x_pos + i) + "" + y_pos);
                    }
                }
                x_pos += change_amt;
            } else if (facing_dir == 3) {
                for (int i = 1; i <= change_amt; i++) {
                    if (list.contains((x_pos - i) + "" + y_pos)) {
                        System.out.println("REPEAT: " + "(" + (x_pos - i) + ", " + y_pos + ")");
                    } else {
                        list.add("" + (x_pos - i) + "" + y_pos);
                    }
                }
                x_pos -= change_amt;
            } else if (facing_dir == 0) {
                for (int i = 1; i <= change_amt; i++) {
                    if (list.contains(x_pos + "" + (y_pos + i))) {
                        System.out.println("REPEAT: " + "(" + x_pos + ", " + (y_pos + i) + ")");
                    } else {
                        list.add("" + x_pos + "" + (y_pos + i));
                    }
                }
                y_pos += change_amt;
            } else {
                for (int i = 1; i <= change_amt; i++) {
                    if (list.contains(x_pos + "" + (y_pos - i))) {
                        System.out.println("REPEAT: " + "(" + x_pos + ", " + (y_pos - i) + ")");
                    } else {
                        list.add("" + x_pos + "" + (y_pos - i));
                    }
                }
                y_pos -= change_amt;
            }
        }
        for (int k = 0; k < list.size(); k++) {
            System.out.println(list.get(k));
        }
    }
    
}