class GradeAvg {
    public static int calc_avg (int [] arr) {
        int avg = 0;
        for (int i = 0; i < arr.length; i++) {
            avg += arr[i];
        }
        return avg / arr.length;
    }
    public static void main (String [] args) {
        int [] arr = {89, 84, 85, 71, 10};
        System.out.println(calc_avg(arr) + "%");
    }

}
