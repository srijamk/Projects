import java.util.ArrayList;
import java.lang.Math;

class xyzMiddle {
    public static boolean xyzMiddle (String str) {
        ArrayList <Integer> array = new ArrayList <Integer> ();
        for (int i = 0; i < str.length() - 2; i++) {
            if (str.substring(i, i + 3).equals("xyz")) {
                array.add(i);
            }
        }
        for (Integer i: array) {
            if (isMiddle(str, i) == true) {
                return true;
            }
        }
        return false;
    }
    public static boolean isMiddle (String str, int integer) {
        int front = 0;
        int back = 0;
        if (integer != 0) {
            front = str.substring(0, integer).length();
        }
        if (integer != str.length() - 1) {
            back = str.substring(integer + 3, str.length()).length();
        }
        return Math.abs(front - back) <= 1;
    }
    public static void main (String [] args) {
        System.out.println(xyzMiddle("AxyzBBB"));
    }
}