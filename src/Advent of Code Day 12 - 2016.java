import java.io.*;
import java.util.*;
import java.util.ArrayList;

class Day_12_Part_1 {
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("input_day_12.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("input_day_12.out")));
        ArrayList <String> instructions = new ArrayList <String>();
        int a = 0;
        int b = 0;
        int c = 0;
        int d = 0;
        int index = 0;
        while (index < 11 ) {
            String instruction = f.readLine();
            f.mark(index);
            
            if (instruction.substring(0, 3).equals("cpy")) {
                
                if (instruction.contains("a") && instruction.contains(" c")) {
                    c = a;
                } else if (instruction.contains("b") && instruction.contains(" c")) {
                    b = c;
                } else {
                    int addition = Integer.parseInt(instruction.substring(instruction.indexOf(" ") + 1, instruction.length() - 2));
                    
                    if (instruction.contains("a")) {
                        a = addition;
                    } else if (instruction.contains("b")) {
                        b = addition;
                    } else if (instruction.contains(" c")) {
                        c = addition;
                    } else {
                        System.out.println("d for da win");
                        d = addition;
                    }
                }
                index++;
            } else if (instruction.substring(0, 3).equals("inc")) {
                if (instruction.contains("a")) {
                    a++;
                } else if (instruction.contains("b")) {
                    b++;
                } else if (instruction.contains(" c")) {
                    c++;
                } else {
                    d++;
                }
                index++;
            } else if (instruction.substring(0, 3).equals("dec")) {
                if (instruction.contains("a")) {
                    a--;
                } else if (instruction.contains("b")) {
                    b--;
                } else if (instruction.contains(" c")) {
                    c--;
                } else {
                    d--;
                }
                index++;
            } else {
                if (instruction.contains("a") && a != 0) {
                    index += Integer.parseInt(instruction.substring(6));
                } else if (instruction.contains("b") && b != 0) {
                    index += Integer.parseInt(instruction.substring(6));
                } else if (instruction.contains(" c") && c != 0) {
                    index += Integer.parseInt(instruction.substring(6));
                } else if (instruction.contains("d") && d != 0) {
                    index += Integer.parseInt(instruction.substring(6));
                } else {
                    if (index == 5) {
                        index += 5;
                    } else {
                        index++;
                    }
                }  
            }
        System.out.println(instruction + ": " + a + ", " + b + ", " + c + ", " + d);
        }
    }
}
