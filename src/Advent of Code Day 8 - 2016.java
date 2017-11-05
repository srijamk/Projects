import java.io.*;
import java.util.*;
import java.util.ArrayList;

class Day_8_Part_1 {
    public static int[][] rect (int[][] screen, int length, int width) {
        int[][] new_screen = screen;
        for (int w = 0; w < width; w++) {
            for (int l = 0; l < length; l++) {
                new_screen[w][l] = 1;
            }
        }
        return new_screen;
    }
    
    public static int[][] rotate_col (int[][] screen, int col, int shift) {
        int[][] new_screen = screen;
        String line = "";
        for (int i = 0; i < 6; i++) {
            line += "" + screen[i][col];
        }
        line += line + line;
        line = line.substring(6 - shift, 12 - shift);
        for (int i = 0; i < 6; i++) {
            new_screen[i][col] = Integer.parseInt("" + line.charAt(i));
        }
        return new_screen;
    } 
    public static int[][] rotate_row (int[][] screen, int row, int shift) {
        int[][] new_screen = screen;
        String line = "";
        for (int i = 0; i < 50; i++) {
            line += "" + screen[row][i];
        }
        line += line + line;
        line = line.substring(50 - shift, 100 - shift);
        for (int i = 0; i < 50; i++) {
            new_screen[row][i] = Integer.parseInt("" + line.charAt(i));
        }
        return new_screen;
    }     
    
    public static String print_screen (int[][] screen) {
        int count = 0;
        for (int j = 0; j < 6; j++) {
            for (int k = 0; k < 50; k++) {
                System.out.print(screen[j][k] + " ");
            }
            System.out.println();
        } 
        return "";
    }

    public static void main (String [] args) throws IOException {
        int[][] screen = new int[6][50];
        BufferedReader f = new BufferedReader(new FileReader("input_day_8.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_8.out")));
        for (int i = 0; i < 145; i++) {
            String line = f.readLine();
            if (line.contains("rect")) {
                int length = Integer.parseInt(line.substring(line.indexOf(' ') + 1, line.indexOf('x')));
                int width = Integer.parseInt(line.substring(line.indexOf('x') + 1));
                System.out.println("Create new rectangle of dimensions " + length + "x" + width);
                screen = rect(screen, length, width);
            } else if (line.contains("rotate column")) {
                int col = Integer.parseInt(line.substring(line.indexOf('=') + 1, line.indexOf('b') - 1));
                int shift = Integer.parseInt(line.substring(line.indexOf('y') + 2));
                System.out.println("Move Column " + col + " by " + shift);
                screen = rotate_col(screen, col, shift);
            } else {
                int row = Integer.parseInt(line.substring(line.indexOf('=') + 1, line.indexOf('b') - 1));
                int shift = Integer.parseInt(line.substring(line.indexOf('b') + 3));
                System.out.println("Move Row " + row + " by " + shift);
                screen = rotate_row(screen, row, shift);                
            }
        }
        System.out.println(print_screen(screen));
          
    }
}