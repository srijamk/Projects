import java.io.*;
import java.util.*;
import java.security.MessageDigest;

class Day_14_Part_1 {
    public static String n_hash (String str) throws Exception{
        String result = str;
        for (int y = 0; y < 2016; y++) {
            result = md5(result);
        }    
        return result;
    }
    
    public static char equal (String str) {
        if ((str.charAt(0) == str.charAt(1)) && (str.charAt(1) == str.charAt(2))) {
            return str.charAt(0);
        }
        return ' ';
    }
    public static char five_equal (String str) {
        
        if ((str.charAt(0) == str.charAt(1)) && (str.charAt(1) == str.charAt(2)) && (str.charAt(2) == str.charAt(3)) && (str.charAt(3) == str.charAt(4))) {
            return str.charAt(0);
        } 
        return ' ';
    }
    
    public static char contains_three (String str) {
        for (int i = 0; i < str.length() - 3; i++) {
            if (equal(str.substring(i, i + 3)) != ' ') {
                return str.charAt(i);
            }
        }
        return ' ';
    }
    public static char contains_five (String str) {
        for (int i = 0; i < str.length() - 5; i++) {
            if (five_equal(str.substring(i, i + 5)) != ' ') {
                return str.charAt(i);
            }
        }
        return ' ';
    }
    public static String md5 (String str) throws Exception{
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(str.getBytes());
        byte[] digest = md.digest();
        String result = "";
        for (int i = 0; i < digest.length; i++) {
            result += String.format("%02x", digest[i] & 0xff);
        }
        return result;
    }
    public static void main (String [] args) throws Exception{

        String word = "abc";
        int count = 1;
        int index = 0;
        while (count <= 64) {
            
           
            String hash = md5(word + index);
            for (int x = 0; x < 2016; x++) {
                hash = md5(hash);
            }
            
            if (contains_three(hash) != ' ') {
                System.out.println(index + ": " + hash);
                char first = contains_three(hash);
                for (int i = index + 1; i <= index + 1000; i++) {
                    String next_hash = n_hash(md5(word + i));
                    if (contains_five(next_hash) == first) {
                        System.out.println("WOOT");
                        count++;
                        break;
                    }
                }
            }
            
            index++;
        }
    }
}