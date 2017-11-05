import java.util.Scanner;
class Recur {
    public static void printWords () {
        Scanner scan = new Scanner(System.in);
        String word = scan.nextLine();
        if (word.equals(".")) {
            System.out.println();
        } else {
            printWords();
        }
        System.out.println(word);
    }
    public static int factorial (int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial (n - 1);
        }
    }
    public static int fibonacci (int n) {
        if (n == 1 || n == 2) {
            return 1;
        } else {
            System.out.println("f(" + (n-1) + "): " + fibonacci(n - 1));
            System.out.println("f(" + (n-2) + "): " + fibonacci(n - 2));
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
    public static void main (String [] args) {
        //printWords();
        //System.out.println(factorial(5));
        System.out.println(fibonacci(5));
    }
}