class notReplace {
  public static String notReplace (String str) {
       String result = "";
       int is_index = str.indexOf("is");
       
       if(is_index == -1) {
           return str;   
       }
       
       
       int start = 0;
       while (start < str.length()) {
           is_index = str.indexOf("is", start);
           if (is_index == -1) {
               result += str.substring(start); 
               break;
           }
           if ((is_index != 0 && (Character.isLetter(str.charAt(is_index - 1))) || (is_index != str.length() - 2 && Character.isLetter(str.charAt(is_index + 2))))) {
               result += str.substring(start, is_index + 2);
           } else {
               result += str.substring(start, is_index + 2) + " not";
           }
           start = is_index + 2;
           System.out.println("Is Index: " + is_index + "\nStart: " + start + "\n");
       }
       return result;
    }
    public static void main (String [] args) {
        //System.out.println(notReplace("Hello there"));
         // System.out.println(notReplace("is Hello there is"));
          System.out.println(notReplace("This is isabell"));
          
        

        
    }
}