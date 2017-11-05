import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;

class Main {

     public static void main (String str[]) throws IOException {
         Scanner scan = new Scanner(System.in);
         System.out.println("Please enter a tweet:");
         String tweet = scan.nextLine();
         
         int hashtags = (tweet.split("#", -1).length-1);
         int attributions = (tweet.split("@", -1).length-1);
         int links = (tweet.split("http://", -1).length-1);
         hashtags -= (tweet.split("# ", -1).length-1);
         hashtags -= (tweet.split("#\t", -1).length-1);
         attributions -= (tweet.split("@ ", -1).length-1);
         attributions -= (tweet.split("@\t", -1).length-1);
         if (tweet.length() > 140) {
           System.out.println("Excess Characters: " + (tweet.length() - 140));
         } else {
           System.out.println("Length Correct");
           System.out.println("Number of Hashtags: " + hashtags);
           System.out.println("Number of Attributions: " + attributions);
           System.out.println("Number of Links: " + links);
         }
     }
}
