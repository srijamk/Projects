import java.io.*;
import java.util.*;

class Strings {
    
    public static String print (String s) {
        return s;
    }
    
    public static String reverse (String s) {
        String result = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            result += s.charAt(i);
        }
        return result;
    }
    
    public static boolean is_palindrome (String s) {
        return s.equals(reverse(s));
    }
    
    public static void main (String [] args) {
        /*
         String s = "Hello World";
         System.out.println(print(s));
         */
        
        /*
         String s = "Hello World";
         System.out.println(reverse(s));
         */
        
        String s = "cat";
        System.out.println(is_palindrome(s));
        
    }
}

