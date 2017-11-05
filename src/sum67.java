class sum67 {
    public static int sum67 (int[] nums) {
        int marker = 0;
        int sum = 0;
        for (int j = 0; j < nums.length; j++) {
            sum += nums[j];
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 6) {
                marker = 1;
            }
            while (marker == 1) {
                if (nums[i] == 7) {
                    marker = 0;
                }
                sum -= nums[i];
            }
        
        }
        return sum;
    }
    public static void main (String [] args) {
        int [] arr = {6, 8, 1, 6, 7};
        System.out.println(sum67(arr));
    }
}