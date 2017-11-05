class sameEnds {
    public static String sameEnds(String string) {
        String result = "";
        int counter = 0;
        for (int i = 0; i < string.length() / 2; i++) {
            //System.out.println("Current: " + (result + string.charAt(i)) + "\nEnd: " + string.substring(string.length() - (i + 1)));
            if ((result + string.charAt(i)).equals(string.substring(string.length() - (i + 1)))) {
                result += string.charAt(i);
                counter = 1;
            } else if (counter == 0 && !((result + string.charAt(i)).equals(string.substring(string.length() - (i + 1))))){
                result += string.charAt(i);
            } else if (counter == 1 && !((result + string.charAt(i)).equals(string.substring(string.length() - (i + 1))))) {
                break;
            }
            if (i == string.length() / 2 - 1 && counter == 0) {
                return "";
            }
        }
        return result;
    }
    public static void main (String [] args) {
        String test = "xavaXYZjava";
        System.out.println(sameEnds(test));
    }
}

