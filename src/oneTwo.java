class oneTwo {
    public static String oneTwo (String str) {
        String result = "";
        for (int i = 0; i < str.length() - 2; i+=3) {
            result += moveTwo(str.substring(i, i + 3));
        }
        return result;
    }
    public static String moveTwo (String str) {
        return "" + str.charAt(1) + str.charAt(2) + str.charAt(0);
    }
    public static void main (String [] args) {
        System.out.println(oneTwo("1234567890"));
    }
}