import java.io.*;
import java.util.*;

class Board {
    public static void main (String [] args) throws IOException {
        BufferedReader f = new BufferedReader(new FileReader("board.in"));
        int n = Integer.parseInt(f.readLine());
        for (int i = 0; i < n; i++) {
            int side = Integer.parseInt(f.readLine());
            for (int j = 0; j < side; j++) {
                for (int k = 0; k < side; k++) {
                    System.out.print("# ");
                }
                System.out.println();
            }
        }
    }
}