
import java.io.*;
import static java.lang.System.*;

import java.util.Scanner;
import java.lang.Math;

/*
class lesson29_notes{
//Lesson 29: Arrays of Strings accessing Methods

 
  public static void main (String str[]) throws IOException {
    
    String movies [ ] = { "The Thing", "I Was a Teenage Werewolf", "The Blob", "Godzilla", "Plan 9 from Outer Space" };
    
    System.out.println( "\n\nThe Movies: ");
    for (int i = 0; i < movies.length; i++ )
    {
      System.out.println(movies[i] + ", First Letter: " + movies[i].charAt(0) + ", Last Letter: " + movies[i].charAt(movies[i].length() - 1));
      
    }
    
  }
  
  
}
*/
class Lesson_29_Activity_Two {

  public static String list [] = {"apple"};
    public static void main(String[] args) {
        for (int i = 0; i < list.length; i++) {
            String reverse_word = "";
            for (int character = list[i].length() - 1; character >= 0; character--) {
                reverse_word += list[i].charAt(character);
            }
            System.out.println(reverse_word);
        }
    }
}