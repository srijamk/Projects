class parenBit {
    public static String parenBit(String str) {
        if (str.length() < 2 && str.indexOf(")") == -1) {
            return "";
        } else {
            if ((str.indexOf("(") == 0 || str.indexOf("(") == -1) && str.indexOf(")") != -1) {
                return "" + str.charAt(0) + parenBit(str.substring(1));
            } else {
                return parenBit(str.substring(1));
            }
        }
        
    }
    public static void main (String [] args) {
        System.out.println(parenBit("xyz(abc)123"));
    }
}