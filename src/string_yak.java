import java.util.Scanner;
import java.util.ArrayList;

class stringYak {
    public static String stringYak (String str) {
        String result = "";
        ArrayList <String> yaks = new ArrayList <String>();
        if (str.contains("yak")) {
            for (int i = 0; i < str.length() - 2; i++) {
                if (str.charAt(i) == 'y' && str.charAt(i + 2) == 'k') {
                    yaks.add("" + i);
                    yaks.add("" + (i + 1));
                    yaks.add("" + (i + 2));
                }
            }
        }
        for (int i = 0; i < str.length(); i++) {
            if (!(yaks.contains("" + i))) {
                result += str.charAt(i);
            }
        }
    return result;
        
    }

    public static void main (String [] args) {
        Scanner scan = new Scanner (System.in);
        System.out.println("Enter a string: ");
        String word = scan.nextLine();
        System.out.println("String without yaks is: " + stringYak(word));
    }
}