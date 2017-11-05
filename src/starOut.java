class starOut {
    public static String starOut (String str) {
        String result = "";
        if (str.charAt(0) != '*' && str.charAt(1) != '*') {
            result += str.charAt(0);
        }
        for (int i = 1; i < str.length() - 1; i++) {
            if (str.charAt(i) != '*' && str.charAt(i + 1) != '*' && str.charAt(i - 1) != '*') {
                result += str.charAt(i);
            }
        }
        if (str.charAt(str.length() - 1) != '*' && str.charAt(str.length() - 2) != '*') {
            result += str.charAt(str.length() - 1);
        }
        return result;
    }
    public static void main (String [] args) {
        String str = "ab**cd";
        System.out.println(starOut(str));
    }
}