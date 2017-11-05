import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Advent_Of_Code_Day_6_Part_2 {
    public static int[][] lights (String line, int[][] config) {
        String cut_line = line.substring(line.indexOf(",") + 1);
        int first_col = Integer.parseInt(cut_line.substring(0, cut_line.indexOf(" ")));
        String new_cut_line = line.substring(line.indexOf("h ") + 2);
        int second_row = Integer.parseInt(new_cut_line.substring(0, new_cut_line.indexOf(",")));
        String newer_cut_line = new_cut_line.substring(new_cut_line.indexOf(",") + 1);
        int second_col = Integer.parseInt(newer_cut_line);
        if (line.indexOf("turn on") != -1) {
            int first_row = Integer.parseInt(line.substring(8, line.indexOf(",")));
            for (int row = first_row; row <= second_row; row++) {
                for (int col = first_col; col <= second_col; col++) {
                    config[row][col]++;
                }
            }
        } else if (line.indexOf("turn off") != -1){
            int first_row = Integer.parseInt(line.substring(9, line.indexOf(",")));
            for (int row = first_row; row <= second_row; row++) {
                for (int col = first_col; col <= second_col; col++) {
                    if (config[row][col] > 0) {
                        config[row][col]--;
                    }
                }
            }
        } else {
            int first_row = Integer.parseInt(line.substring(7, line.indexOf(",")));
            for (int row = first_row; row <= second_row; row++) {
                for (int col = first_col; col <= second_col; col++) {
                    config[row][col] += 2;
                }
            }
        }
        return config;
    }
    public static void main (String [] args) {
        int[][] config = new int [1000][1000];
        int sum = 0;
        int[][] result = new int [1000][1000];
        try {
            FileInputStream in = new FileInputStream("advent_of_code_day_6_part_1_input.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String line;
            int count = 0;
            while((line = br.readLine()) != null) {
                result = lights(line, config);
                System.out.println((300 - count) + " away from success! Error on the line with " + line.substring(0, 3));
                count++;
            }
            
        } catch(Exception e) {
            System.out.println(e);
        }
        for (int row = 0; row < result.length; row++) {
            for (int col = 0; col < result[0].length; col++) {
                sum += result[row][col];
            }
        }
        System.out.println("Total brightness: " + sum);
    }
}