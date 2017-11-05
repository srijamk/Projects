import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Advent_Of_Code_Day_6_Part_1 {
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
                    config[row][col] = 1;
                }
            }
        } else if (line.indexOf("turn off") != -1){
            int first_row = Integer.parseInt(line.substring(9, line.indexOf(",")));
            for (int row = first_row; row <= second_row; row++) {
                for (int col = first_col; col <= second_col; col++) {
                    config[row][col] = 0;
                }
            }
        } else {
            int first_row = Integer.parseInt(line.substring(7, line.indexOf(",")));
            for (int row = first_row; row <= second_row; row++) {
                for (int col = first_col; col <= second_col; col++) {
                    if (config[row][col] == 0) {
                        config[row][col] = 1;
                    } else {
                        config[row][col] = 0;
                    }
                }
            }
        }
        return config;
    }
    public static ArrayList <Integer> findstarts (String line) {
        ArrayList <Integer> result = new ArrayList <Integer>();
        String cut_line = line.substring(line.indexOf(",") + 1);
        int first_row;
        int first_col = Integer.parseInt(cut_line.substring(0, cut_line.indexOf(" ")));
        String new_cut_line = line.substring(line.indexOf("h ") + 2);
        int second_row = Integer.parseInt(new_cut_line.substring(0, new_cut_line.indexOf(",")));
        String newer_cut_line = new_cut_line.substring(new_cut_line.indexOf(",") + 1);
        int second_col = Integer.parseInt(newer_cut_line);
        if (line.indexOf("turn on") != -1) {
            first_row = Integer.parseInt(line.substring(8, line.indexOf(",")));
        } else if (line.indexOf("turn off") != -1) {
            first_row = Integer.parseInt(line.substring(9, line.indexOf(",")));
        } else {
            first_row = Integer.parseInt(line.substring(7, line.indexOf(",")));
        }
        result.add(first_row);
        result.add(second_row);
        result.add(first_col);
        result.add(second_col);
        return result;
    }
    public static void main (String [] args) {
        int sum = 0;
        
        int[][] config = new int[1000][1000];
        int[][] result = new int[1000][1000];
        ArrayList <String> errors = new ArrayList <String>();
        
        try {
            FileInputStream in = new FileInputStream("advent_of_code_day_6_part_1_input.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String line;
            int count = 0;
            while((line = br.readLine()) != null) {
                count = 0;
                result = lights(line, config);
                System.out.println("Line is " + line);
                for (int r = 0; r < result.length; r++) {
                    for (int c = 0; c < result[0].length; c++) {
                        if (result[r][c] == 1) {
                            count++;
                        }
                    }
                }    
                System.out.println(count);
                //System.out.println((300 - count) + " away from success! Error on the line with " + strLine.substring(0, 3));
            }
            
        } catch(Exception e) {
            System.out.println(e);
        }
  
        /*
        result = lights("toggle 756,965 through 812,992", config);
        for (int r = 0; r < result.length; r++) {
            for (int c = 0; c < result[0].length; c++) {
                if (result[r][c] == 1) {
                    sum++;
                }
            }
        }   
        */
        for (String line: errors) {
            System.out.println(line);
        }
        System.out.println("Lit lights: " + sum);
    }
}