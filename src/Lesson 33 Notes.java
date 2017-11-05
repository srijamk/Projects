import java.util.Scanner;
import java.io.*;
import java.lang.Math;

class Lesson_33_Activity_Five {
  
    public static void randomize (int [] nums) {
        for (int i = 0; i < nums.length; i++) {
            nums[i] = ((int) (Math.random() * 90) + 10);
        }
    }
  
    public static void main(String[] args) {
        int [] nums = {1, 2, 3, 4, 5};
        randomize(nums);
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}