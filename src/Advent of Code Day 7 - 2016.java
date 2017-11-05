import java.io.*;
import static java.lang.System.*;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.lang.Math;
import java.util.ArrayList;

class Day_7_Part_1 {
    public static boolean is_valid (String s) {
        return (s.charAt(0) == s.charAt(2)) && (s.charAt(0) != s.charAt(1)) && !s.contains(" ");
    }
    
    public static String inverse (String s) {
        String result = "";
        result += s.charAt(1);
        result += s.charAt(0);
        result += s.charAt(1);
        return result;
    }

    public static void main (String [] args) throws IOException {
        System.out.println(inverse("mgm"));
        BufferedReader f = new BufferedReader(new FileReader("input_day_7.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_7.out")));    
        int count = 0;
        for (int i = 0; i < 2000; i++) {
            String line = f.readLine();
            String not_hypernet = "";
            String hypernet = "";
            boolean in_hypernet = false;
            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == '[') {
                    in_hypernet = true;
                    not_hypernet += "    ";
                } else if (line.charAt(j) == ']') {
                    in_hypernet = false;
                    hypernet += "    ";
                }
                if (in_hypernet && line.charAt(j) != '[') {
                    hypernet += line.charAt(j);
                }
                if (!in_hypernet && line.charAt(j) != ']') {
                    not_hypernet += line.charAt(j);
                }
            }
            for (int k = 0; k < not_hypernet.length() - 2; k++) {
                if (is_valid(not_hypernet.substring(k, k + 3)) && hypernet.contains(inverse(not_hypernet.substring(k, k + 3)))) {
                    System.out.println(i + ": " + not_hypernet.substring(k, k + 3));
                    count++;
                    break;
                }
            }
            //System.out.println(i + not_hypernet);
        }
        System.out.println(count);
    }
/*
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_7.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_7.out")));    
        int count = 0;
        for (int i = 0; i < 2000; i++) {
            String line = f.readLine();
            boolean outside = true;
            boolean yay = false;
            ArrayList <String> out_list = new ArrayList <String>();
            ArrayList <String> in_list = new ArrayList <String>();
            for (int j = 0; j < line.length() - 3; j++) {
                if (line.charAt(j) == '[') {
                    outside = false;
                }
                if (line.charAt(j) == ']') {
                    outside = true;
                }
                if (outside && line.charAt(j) == line.charAt(j + 2) && line.charAt(j) != line.charAt(j + 1)) {
                    out_list.add(line.substring(j, j + 3));
                }                
                if (!outside && line.charAt(j) == line.charAt(j + 2) && line.charAt(j) != line.charAt(j + 1)) {
                    in_list.add(line.substring(j, j + 3));
                }
            }
            for (String item: out_list) {
                if (in_list.contains(inverse(item))) {
                    System.out.println(line);
                    yay = true;

                }
            }
            if (yay) {
                count++;
            }
        }
        System.out.println(count);    
    }
    */
}