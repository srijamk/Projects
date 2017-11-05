import java.lang.Math;
import java.util.ArrayList;
class notAlone {
    public static int[] notAlone(int[] nums, int val) {
        ArrayList <Integer> list = new ArrayList <Integer>();
        if ((nums[0] == val && nums[1] != val) || (nums[0] != val && nums[1] == val)) {
            list.add(nums[1]);
        } else if ((nums[0] == val && nums[1] == val) || (nums[0] != val && nums[1] != val)) {
            list.add(nums[0]);
        }
        
        for (int i = 1; i < nums.length - 1; i++) {
            if (nums[i] == val && nums[i - 1] != val && nums[i + 1] != val) {
                list.add(Math.max(nums[i - 1], nums[i + 1]));
            } else {
                list.add(nums[i]);
            }
        }
        if ((nums[nums.length - 1] == val && nums[nums.length - 2] != val) || (nums[nums.length - 1] != val && nums[nums.length - 2] == val)) {
            list.add(nums[nums.length - 1]);
        } else if ((nums[nums.length - 1] == val && nums[nums.length - 2] == val) || (nums[nums.length - 1] != val && nums[nums.length - 2] != val)) {
            list.add(nums[nums.length - 2]);
        }        
        int [] arr = new int [list.size()];
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return arr;
    }
    public static void main (String [] args) {
        int [] arr = {1, 5, 2, 4, 2, 5, 6};
        System.out.println(notAlone(arr, 5));
    }
}
