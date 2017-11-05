import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.lang.Math;

class Main {
    public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);
        System.out.println("Please Enter the Cost of the Item:");
        double cost = scan.nextDouble();
        System.out.println("Please Enter the Amount Paid: ");
        double amount_paid = scan.nextDouble();
        double change_owed = ((double) (amount_paid * 100 - cost * 100));
        System.out.println("Change Owed: " + change_owed / 100.0);
        
        System.out.println("Quarters: " + (int) ((change_owed * 100 / 25) / 100.0));
        double quarter_amount = ((double) ((int) ((change_owed * 100 / 25) / 100)) * 25);
        double no_quarters = change_owed - quarter_amount;
        
        System.out.println("Dimes: " + (int) no_quarters / 10); 
        double dime_amount = ((double) ((int) ((no_quarters * 100 / 10) / 100)) * 10);
        double no_dimes = no_quarters - dime_amount;
        
        System.out.println("Nickels: " + (int) (no_dimes / 5));
        double nickel_amount = ((double) ((int) ((no_dimes * 100 / 5) / 100)) * 5);
        double no_nickels = no_dimes - nickel_amount;
        
        System.out.println("Pennies: " + (int) no_nickels);
    }    
}