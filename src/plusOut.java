import java.util.ArrayList;

class plusOut {
    public static String plusout (String str, String word) {
        String result = "";
        ArrayList <Integer> arr = new ArrayList <Integer> ();
        for (int i = 0; i < str.length() - word.length() + 1; i++) {
            if (str.substring(i, i + word.length()).equals(word)) {
                for (int j = i; j < i + word.length(); j++) {
                    arr.add(j);
                }
            } 
        }
        for (int i = 0; i < str.length(); i++) {
            if ((arr.contains(i))) {
                result += "" + str.charAt(i);
            } else {
                result += "+";
            }
        }
        return result;
    }
    public static void main (String [] args) {
        System.out.println(plusout("xyzxyx", "xy"));
    }
}


