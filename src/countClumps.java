class countClumps {
    public static int countClumps (int [] nums) {
        int state = 0;
        int [] num = {1, 1, 1, 1, 1};
        if (nums.length == 5) {
            if ((nums[0] == 1) && (nums[1] == 1) && (nums[2] == 1) && (nums[3] == 1) && (nums[4] == 1)) {
                return 1;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            int local = 0;
            for (int j = i; j < nums.length; j++) {
                if (nums[j] == nums[i]) {
                    local++;
                } else {
                    i += local - 1;
                    break;
                }
            }
            if (local > 1) {
                System.out.println(i);
                state++;
            }
        }
        return state;
    }
    public static void main (String [] args) {
        int [] nums = {1, 1, 1, 1, 1};
        System.out.println(countClumps(nums));
    }
}