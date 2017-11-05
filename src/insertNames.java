import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
class Main {
    public static String titleCase (String s) {
        return ("" + s.charAt(0)).toUpperCase() + s.substring(1).toLowerCase();
    }
    public static void main (String [] args) {
        String input = "";
        ArrayList <String> list = new ArrayList <String>();
        Scanner scan = new Scanner(System.in);
        while (!(input.toLowerCase().equals("stop"))) {
            System.out.println("Enter the next name: ");
            input = scan.nextLine();
            list.add(titleCase(input));
        }
        list.remove(list.size() - 1);
        String temp;
        for (int i = 0; i < list.size(); i++) {
            for (int j = i + 1; j < list.size(); j++){
                if (list.get(i).compareTo(list.get(j)) > 0) {
                    temp = list.get(i);
                    list.set(i, list.get(j));
                    list.set(j, temp);   
                }
            }
        }
        System.out.println(list);
    }
}