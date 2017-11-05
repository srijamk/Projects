import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.lang.Math;
import java.util.ArrayList;
import java.util.Arrays;

class Day_6_Part_1 {
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_6.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_6.out")));    
        int [] list = new int [26];
        for (int i = 0; i < 624; i++) {
            String line = f.readLine();
            list[(int)line.charAt(7) - 97]++;
        }
        for (int j = 0; j < 26; j++) {
            System.out.println(list[j]);
        }
    }
}