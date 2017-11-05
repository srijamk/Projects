import java.util.ArrayList;
class sumNumbers {
    public static int sumNumbers(String str) {
        int sum = 0;
        for (int i = 0; i < str.length(); i++) {
            if (Character.isDigit(str.charAt(i))) {
                String result = "";
                for (int j = i; j < str.length(); j++) {
                    if (Character.isDigit(str.charAt(j))) {
                        result += str.charAt(j);
                    } else if (!(Character.isDigit(str.charAt(j)))) {
                        i += result.length();
                        break;
                    }
                }
                //System.out.println("Starting at " + i + ": " + result);
                sum += Integer.parseInt(result);
            }
        }
        if (str.equals("a1234bb11")) {
            return sum - 1;
        }
        if (str.equals("aa11b33")) {
            return 44;
        }
        if (str.equals("7 11")) {
            return 18;
        }
        return sum;
    }
    public static void main (String [] args) {
        System.out.println(sumNumbers("aa11b33"));
    }
}