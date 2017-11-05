import java.util.Scanner;

class Lesson_30_Activity {
     
   /*
    * Your code should end with the following array modified as the 
    * instructions above specify. You may modify the elements in 
    * this list but make sure you do not add or remove anything from it. 
   */
    public static String [] list = {"every", " near ing ", " checking", "food ", "stand", "value "};
        public static void main(String[] args) {
            for (int i = 0; i < list.length; i++) {
                list[i] = list[i].replace(" ", "");
                System.out.println(list[i]);
                    }
                }
            }