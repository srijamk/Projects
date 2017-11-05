import java.lang.Integer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
class Advent_of_Code_Day_7 {
    //ArrayList <String> vars = new ArrayList <String>();
    //ArrayList <String> vals = new ArrayList <String>();
    public void answer () {
        try {
            FileInputStream in = new FileInputStream("advent_day_7_part_1_input.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(in));        
            String line;
            int count = 0;
            while ((line = br.readLine()) != null) {
                
                if (line.substring(0, line.indexOf(" ")).matches("-?\\d+(\\.\\d+)?") && line.substring(line.indexOf(" "), line.indexOf(" ") + 3).equals(" ->")) {
                    //System.out.println(line.substring(line.indexOf("> ")));
                    //vars.add(line.substring(line.indexOf("> ") + 2));
                    //vals.add(line.substring(0, line.indexOf("-")));
                }
                count++;
            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void main (String [] args) {
        answer();
        //System.out.println(vars.get(0));
    }
}