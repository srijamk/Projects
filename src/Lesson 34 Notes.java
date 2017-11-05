import java.util.Scanner;

class Lesson_34_Activity_Two {
  
   public static void doStuff (int a[], int b) {
    if (b < a.length) {
        for (int i = b; i < a.length; i++) {
            a[i] = a[i] * 2;
        }
    }
}
}