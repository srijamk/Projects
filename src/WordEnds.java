import java.util.ArrayList;

class WordEnds {
    public static String WordEnds (String str, String word) {
        ArrayList <Integer> array = new ArrayList <Integer> ();
        String result = "";
        for (int i = 0; i < str.length() - word.length() + 1; i++) {
            if (str.substring(i, i + word.length()).equals(word)) {
                array.add(i);
            }
        }
        
        for (Integer i: array) {
            if (i > 0) {
                result += str.charAt(i - 1);
            }
            if ((i + word.length() - 1) != (str.length() - 1)) {
                result += str.charAt(i + word.length());
            }
        }
        
        return result;
        
    }
    public static void main (String [] args) {
        System.out.println(WordEnds("abc1abc1abc", "abc"));
    }
}