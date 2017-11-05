import java.util.ArrayList;

class tenRun {
    public static int tenRun (int [] nums) {
        ArrayList <Integer> arr = new ArrayList <Integer> ();
        for (int i = 0; i < nums.length - 1; i++) {
            int newten = i;
            if (nums[i] % 10 == 0) {
                newten = i;
                for (int j = i; j < )
            }
            
        }
        for (int k = 0; k < arr.size() - 1; k++) {
            for (int j = arr.get(k); j < arr.get(k + 1); j++) {
                nums[j] = nums[arr.get(k)];
            }
        }
        for (int l = 0; l < nums.length; l++) {
            System.out.println(nums[l]);
        }
        return 1;
    }
    public static void main (String [] args) {
        int [] arr = {1, 10, 5};
        System.out.println(tenRun(arr));
    }
}

