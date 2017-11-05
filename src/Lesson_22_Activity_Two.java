import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

class Lesson_22_Activity_Two {
  
    public static void main (String str[]) throws IOException {
        Scanner scan = new Scanner (System.in);
        System.out.println("Enter a word: ");
        String word = scan.nextLine();
        // loop n times, for every n increment tab_count by 1
        int index = 0;
        while (index < word.length()) {
          String tab_amount = "";
          for (int x = 0; x < index; x++) {
            tab_amount += "\t";
          }
          System.out.println(tab_amount + word.substring(index, index + 1));
          index++;
        }
    }
}
