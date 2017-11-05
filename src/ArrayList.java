import java.util.ArrayList;
import java.util.Scanner;
class Main {
    public static void main (String [] args) {
        ArrayList <String> list = new ArrayList <String> ();
        System.out.println("Please enter words, enter STOP to stop the loop.");
        Scanner scan = new Scanner (System.in);
        String word = scan.nextLine();
        while (!(word.equals("STOP"))) {
            list.add(word);
            word = scan.nextLine();
        }
        System.out.println(list.size());
        System.out.println(list);
        if (list.size() > 2) {
            list.remove(0);
            list.remove(list.size() - 1);
        }
        System.out.println(list);
    }
}