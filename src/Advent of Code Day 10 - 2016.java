import java.io.*;
import static java.lang.System.*;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.lang.Math;
import java.util.ArrayList;

class Day_10_Part_1 {
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_10.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_10.out")));   
        int [] first = new int [3];
        int [] second = new int [3];
        for (int i = 0; i < 6; i++) {
            String line = f.readLine();
            if (line.substring(0, 6).equals("value")) {
                int value = Integer.parseInt(line.substring(line.indexOf(" ") + 1, line.indexOf(" ") + 2));
                int recipient = Integer.parseInt("" + line.charAt(line.length() - 1));
                if (first[recipient] == 0) {
                    first[recipient] = value;
                } else {
                    second[recipient] = value;
                }
            }
        }
        for (int j = 0; j < first.length; j++) {
            System.out.println(first[j]);
        }
    }
}