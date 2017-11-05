import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class Main {
    public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);
        
        int incorrect_characters = 0;
        String [] list = {"!", "@", "#", "$", "^", "&", "(", ")", "<", ">", ".", ",", "{", "}", "|", "/", "-", "_", "+", "=", "[", "]", ";", ":", "?"};
        
        System.out.println("Enter the first String: ");
        String first_str = scan.nextLine();
        System.out.println("Enter the replacement String: ");
        String replacement_str = scan.nextLine();
        
        for (int x = 0; x < list.length; x++) {
            if (first_str.contains(list[x])) {
                incorrect_characters = 1;
            }
        }
        
        if (incorrect_characters == 0) {
            if (first_str.contains("*")) {
                System.out.println(first_str.replace("*", replacement_str));
                
            } else {
                System.out.println("Error: no *");        
            } 
        } else {
            System.out.println("Error: Incorrect characters");
        }   
    }
}