import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.lang.Math;
import java.util.ArrayList;
import java.util.Arrays;
class Day_4_Part_1 {
    public static int indexOf (int n, int[]list) {
        for (int i = 0; i < list.length; i++) {
            if (list[i] == n) {
                return i;
            }
        }
        return -1;
    }
    public static int max (int [] freq) {
        int max = 0;
        int result = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > max) {
                max = freq[i];
                result = i;
            }
        }
        return result;
    }
    public static String caesar_cipher (String sentence, int id) {
        id = id % 26;
        char [] characters = new char[sentence.length()];
        for (int i = 0; i < sentence.length(); i++) {
            if (sentence.charAt(i) == '-') {
                characters[i] = ' ';
            } else {
                if ((int)sentence.charAt(i) + id <= 122) {
                    characters[i] = (char)((int)sentence.charAt(i) + id);
                } else {
                    characters[i] = (char) (97 + id - (123 - (int)sentence.charAt(i)));
                }
            }
        }
        String result = "";
        for (int j = 0; j < characters.length; j++) {
            result += characters[j];
        }
        return result;
    }
    /*
     * Advent of Code Day 4: Part 1
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_4.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_4.out")));    
        int count = 0;
        
        for (int i = 0; i < 1091; i++) {
            int[] freq = new int [26];
            
            String[] freq_letters = new String [26];
            String line = f.readLine();
            int start_char = line.indexOf('[');
            boolean real = true;
            String letters = line.substring(line.indexOf('[') + 1, line.length() - 1);
            
            for (int k = 0; k < start_char; k++) {
                int convert = (int)line.charAt(k);
                if (convert >= 97 && convert <= 122) {
                    freq[(int)line.charAt(k) - 97]++;
                }
            }
            
            
            String ans = "";
            for (int j = 1; j <= 5; j++) {
                int max = max(freq);
                ans += (char)(max + 97);
                freq[max] = 0;
            }
            if (ans.equals(letters)) {
                count += Integer.parseInt(line.substring(start_char - 3, start_char));
            }
            
        }
        System.out.println(count);
        */
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_4.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_4.out")));
        for (int i = 0; i < 1901; i++) {
            String line = f.readLine();
            int start_char = line.indexOf('[');
            int sector_id = Integer.parseInt(line.substring(start_char - 3, start_char));
            System.out.println(sector_id + ": " + caesar_cipher(line.substring(0, start_char - 3), sector_id));
        }
    }
}

