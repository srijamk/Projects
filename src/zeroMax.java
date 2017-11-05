class zeroMax {
    public static int [] zeroMax (int [] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                nums[i] = oddMax(nums, i);
            }
        }
        return nums;
    }
    public static int oddMax (int [] nums, int index) {
        int highest_odd = 0;
        for (int i = index; i < nums.length; i++) {
            if (nums[i] % 2 != 0 && nums[i] > highest_odd) {
                highest_odd = nums[i];
            }
        }
        return highest_odd;
    } 
    public static void main (String [] args) {
        int [] arr = {0, 5, 0, 3};
        System.out.println(zeroMax(arr));
    }
}