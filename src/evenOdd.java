import java.util.ArrayList;

class evenOdd {
    public int [] evenOdd(int[] nums) {
        int [] arr = new int [nums.length];
        ArrayList <Integer> evens = new ArrayList <Integer> ();
        ArrayList <Integer> odds = new ArrayList <Integer> ();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                evens.add(i);
            } else {
                odds.add(i);
            }
        }
        for (int i = 0; i < evens.size(); i++) {
            arr[i] = nums[evens.get(i)];
        }
        for (int i = evens.size(); i < evens.size() + odds.size(); i++) {
            arr[i] = nums[odds.get(i - evens.size())];
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    return arr;
    }
    
    public static  void main (String [] args) {
        int [] arr = {1, 0, 1, 0, 1, 0};
        System.out.println(evenOdd(arr));
    }
}