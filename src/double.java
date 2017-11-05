import java.util.Scanner;
class Double {
    public static int Double (int num) {
        return num * 2;
    }
    
    public static void main (String [] args) {
        Scanner scan = new Scanner (System.in);
        int a = scan.nextInt();
        System.out.println(Double(a));
    }
}