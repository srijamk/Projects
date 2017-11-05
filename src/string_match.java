import java.util.Scanner;

class StringMatch {
    public static int stringMatch(String a, String b) {
        int counter = 0;
        if (a.length() < b.length()) {
            for (int i = 0; i < a.length() - 1; i++) {
                if (a.substring(i, i + 2).equals(b.substring(i, i + 2))) {
                    counter++;
                }
            }
        } else {
            for (int i = 0; i < b.length() - 1; i++) {
                if (a.substring(i, i + 2).equals(b.substring(i, i + 2))) {
                    counter++;
                }
            }    
        }
        return counter;
    }

    public static void main (String [] args) {
        Scanner scan = new Scanner (System.in);
        System.out.println("Enter two strings: ");
        String a = scan.nextLine();
        String b = scan.nextLine();
        System.out.println(stringMatch(a, b));
    }

}