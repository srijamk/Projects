class Rounding {
    public static int roundIt(double a) {
        if ((a - (int) a) >= 0.5) {
            return (int) a + 1;
        } else {
            return (int) a;
        }
    }
    public static void main (String [] args) {
        System.out.println(roundIt(4.6));
        System.out.println(roundIt(4.2));
        System.out.println(roundIt(6));
        System.out.println(roundIt(6.6));
    }
}