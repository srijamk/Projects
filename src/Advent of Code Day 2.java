import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileInputStream;
/*
class Santa_Part_1 {
    public static int paper (int a, int b, int c) {
        int first_side = 2 * a * b;
        int second_side = 2 * a * c;
        int third_side = 2 * b * c;   
        return Math.min(Math.min(first_side / 2, second_side / 2), third_side / 2) + first_side + second_side + third_side;
    }
    
    public static void main (String[] args) {
        int counter = 0;
        BufferedReader br = null;
        try {
            FileInputStream fstream = new FileInputStream("advent_of_code_day_2_file.txt");
            br = new BufferedReader(new InputStreamReader(fstream)); 
            String line;
            
            while ((line = br.readLine()) != null) {
                String [] dim = line.split("x", 3);
                int a = Integer.parseInt(dim[0]);
                int b = Integer.parseInt(dim[1]);
                int c = Integer.parseInt(dim[2]);
                counter += paper(a, b, c);
            }
            br.close(); 
        } catch (Exception e) {
        }
        System.out.println("The elves should order a total of " + counter + " square feet of wrapping paper. ");
    }
    
}
*/

class Santa_Part_2 {
    public static int ribbon (int a, int b, int c) {
        int first_side = 2 * a + 2 * b;
        int second_side = 2 * a + 2 * c;
        int third_side = 2 * b + 2 * c;
        if ((Math.min(Math.min(first_side, second_side), third_side)) == first_side) {
            return first_side + a * b * c;
        } else if (Math.min(Math.min(first_side, second_side), third_side) == second_side) {
            return second_side + a * b * c;
        } else {
            return third_side + a * b * c;
        }
        
    }
        public static void main (String[] args) {
            
        
        int counter = 0;
        BufferedReader br = null;
        try {
            FileInputStream fstream = new FileInputStream("advent_of_code_day_2_ribbon.txt");
            br = new BufferedReader(new InputStreamReader(fstream)); 
            String line;
            
            while ((line = br.readLine()) != null) {
                String [] dim = line.split("x", 3);
                int a = Integer.parseInt(dim[0]);
                int b = Integer.parseInt(dim[1]);
                int c = Integer.parseInt(dim[2]);
                counter += ribbon(a, b, c);
            }
            br.close(); 
        } catch (Exception e) {
        }
        System.out.println("The elves should order a total of " + counter + " square feet of wrapping paper. ");
        
    }
    

}