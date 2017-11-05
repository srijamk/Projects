class strCopies {
    public static boolean strCopies(String str, String sub, int n) {
        int counter = 0;
        if (str.length() < sub.length()) {
            return false;
        } else {
            if (str.substring(0, sub.length()).equals(sub)) {
                counter++;
                System.out.println(counter);
                return counter >= n || strCopies(str.substring(1), sub, n);
            } else {
                return counter >= n || strCopies(str.substring(1), sub, n);
            }
        }
        
    }
    public static void main (String [] args) {
        System.out.println(strCopies("catcowcat", "cat", 2));
    }
}