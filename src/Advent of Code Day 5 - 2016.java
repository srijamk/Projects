//package digest;

import java.security.MessageDigest;

class Day_5_Part_1 {
    public static String md5 (String str) throws Exception{
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(str.getBytes());
        byte[] digest = md.digest();
        String result = "";
        for (int i = 0; i < digest.length; i++) {
            result += String.format("%02x", digest[i] & 0xff);
        }
        return result;
    }
    public static void main (String [] args) throws Exception{
        String original = "wtnhxymk";
        String [] result = new String [8];
        int num = 1;
        int i = 0;
        while (num <= 8) {
            if (md5(original + i).substring(0, 5).equals("00000")) {
                if ((int)md5(original + i).charAt(5) >= 48 && (int)md5(original + i).charAt(5) <= 55 && result [Integer.parseInt("" + md5(original + i).charAt(5))] == null) {
                    result [Integer.parseInt("" + md5(original + i).charAt(5))] = "" + md5(original + i).charAt(6);
                    for (int j = 0; j < result.length; j++) {
                        System.out.print(result[j]);
                    }
                    System.out.println();
                    num++;
                }
            }
            i++;
        }
        for (int j = 0; j < result.length; j++) {
            System.out.print(result[j]);
        }
    }
}