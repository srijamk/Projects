import java.util.ArrayList;

class fix34 {
    public static int[] fix34(int[] nums) {
        int [] result = new int [nums.length];
        ArrayList <Integer> list = new ArrayList <Integer> ();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 3) {
                result[i] = 3; 
            } 
            if (nums[i] != 3 && nums[i] != 4) {
                list.add(nums[i]);
            }
        }
        for (int j = 0; j < result.length; j++) {
            if (nums[j] == 3) {
                result[j + 1] = 4;
            }
        }
        int counter = 0;
        for (int k = 0; k < result.length; k++) {
            if (result[k] != 3 && result[k] != 4) {
                result[k] = list.get(counter);
                counter++;
            }
        }
        return result;
    }
    public static void main (String [] args) {
        int [] arr = {1, 3, 1, 4};
        System.out.println(fix34(arr));
    }
}