class Lesson_17_Activity {
    public static boolean isSorted (int [] a) {
        for (int i = 0; i < a.length - 1; i++) {
            if (a[i] > a [i + 1]) {
                return false;
            }    
        }
        return true;
    }    
    public static int binarySearch (int [] a, int b) {
        int low = 0;
        int high = a.length;
        while (high >= low) {
            if (b > a[(high + low) / 2]) {
                low = (high + low) / 2;
                System.out.println(((high + low) / 2));
            } else if (b < a[(high + low) / 2]) {
                high = (high + low) / 2;
            } else if (b == a[(high + low) / 2]) {
                return (high + low) / 2;
            }
            if (high - low == 1 && b != a[low] && b != a[high]) {
                return -1;
            }
        }
        return -1;
    }
    public static void main (String [] args) {
        int [] a = {1, 2, 3, 4};
        int [] b = {2, 6, 8, 10};
        int [] c = {5, 2, 7, 12};
        System.out.println(binarySearch(a, 1));
        // System.out.println(isSorted(b));
        // System.out.println(isSorted(c));
    }
}