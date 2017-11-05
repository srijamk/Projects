import java.util.ArrayList;

class post4 {
    public static int[] post4 (int[] nums) {
        ArrayList <Integer> arrlist = new ArrayList <Integer>();
        int last_4 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 4) {
                last_4 = i;
            }
        }
        for (int j = last_4 + 1; j < nums.length; j++) {
            arrlist.add(nums[j]);
        }
        int [] arr = new int [arrlist.size()];
        for (int k = 0; k < arr.length; k++) {
            arr[k] = arrlist.get(k);
        }
        return arr;
    }
    public static void main (String [] args) {
        int [] arr = {2, 4, 1, 2};
        System.out.println(post4(arr));
    }
}