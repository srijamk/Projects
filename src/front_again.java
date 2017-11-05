import java.util.Scanner;

class front {
    public static boolean frontAgain(String str) {
        if (str.length() < 2) {
            return false;
        } else if (str.length() == 2) {
            return true;
        } else {
            return str.substring(0, 2).equals(str.substring(str.length() - 2));
            
        }
    }
    public static void main (String [] args) {
        Scanner scan = new Scanner (System.in);
        System.out.println("Enter a string: ");
        String str = scan.nextLine();
        System.out.println(frontAgain(str));
    }
}