import java.io.*;
import java.util.*;
import java.util.ArrayList;
class wormhole {
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("wormhole.in"));
        BufferedWriter out = new BufferedWriter(new PrintWriter(new FileWriter("wormhole.out")));
        int N = Integer.parseInt(f.readLine());
        ArrayList <String []> points = new ArrayList <String []> ();
        for (int i = 0; i < N; i++) {
            points.add(f.readLine().split(" "));
        }
        while (true) {
            
        }
        
    }
}
