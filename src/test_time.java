import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;

public class test_time {
    public static void main (String str[]) throws IOException {
        Time t1 = new Time (1, 19);
        System.out.println("time1: " + t1.toString());
        System.out.println("convert time1 to standard time: " + t1.convert());
        t1.increment();
        System.out.println("time1 incremented 60 times: " + t1.toString());
    }
}