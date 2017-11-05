import java.io.*;
import static java.lang.System.*;
import java.util.Scanner;
import java.lang.Math;

class Main2 {
  public static void main (String str[]) throws IOException {
    Scanner scan = new Scanner (System.in);
    
    String month_word = "";
    String day_word = "";
    String horoscope = "";
    System.out.println("What month were you born in? (number)");
    int month = scan.nextInt();
    System.out.println("What day (number)");
    int day = scan.nextInt();
    if (month < 1 || month > 12) {
      month_word = "error";  
    }
    if (month == 1) {
      month_word = "January";
      if (day <= 19) {
        horoscope = "Capricorn";  
      } else {
        horoscope = "Aquarius";
      }
    } 
    else if (month == 2) {
      month_word = "February";
      if (day <= 18) {
        horoscope = "Aquarius";
      } else {
        horoscope = "Pisces";
      }
    }
    else if (month == 3) {
      month_word = "March";
      if (day <= 20) {
        horoscope = "Pisces";
      } else {
        horoscope = "Aries";
      }
    }
    else if (month == 4) {
      month_word = "April";
      if (day <= 19) {
        horoscope = "Aries";
      } else {
        horoscope = "Taurus";
      }
    }
    else if (month == 5) {
      month_word = "May";
      if (day <= 20) {
        horoscope = "Taurus";
      } else {
        horoscope = "Gemini";
      }
    }
    else if (month == 6) {
      month_word = "June";
      if (day <= 20) {
        horoscope = "Gemini";
      } else {
        horoscope = "Cancer";
      }
    }   
    else if (month == 7) {
      month_word = "July";
      if (day <= 22) {
        horoscope = "Cancer";
      } else {
        horoscope = "Leo";
      }
    }
    else if (month == 8) {
      month_word = "August";
      if (day <= 22) {
        horoscope = "Leo";
      } else {
        horoscope = "Virgo";
      }
    }
    else if (month == 9) {
      month_word = "September";
      if (day <= 22) {
        horoscope = "Virgo";
      } else {
        horoscope = "Libra";
      }
    }
    else if (month == 10) {
      month_word = "October";
      if (day <= 22) {
        horoscope = "Libra";
      } else {
        horoscope = "Scorpio";
      }
    }
    else if (month == 11) {
      month_word = "November";
      if (day <= 21) {
        horoscope = "Scorpio";
      } else {
        horoscope = "Sagittarius";
      }
    }    
    else if (month == 12) {
      month_word = "December";
      if (day <= 21) {
        horoscope = "Sagittarius";
      } else {
        horoscope = "Capricorn";
      }
    }
    if (day < 1 || day > 31) {
      day_word = "error";
    }
    if (day == 1) {
      day_word = "first";
    }
    else if (day == 2) {
      day_word = "second";
    }
    else if (day == 3) {
      day_word = "third";
    }
    else if (day == 4) {
      day_word = "fourth";
    }    
    else if (day == 5) {
      day_word = "fifth";
    }    
    else if (day == 6) {
      day_word = "sixth";
    }    
    else if (day == 7) {
      day_word = "seventh";
    }    
    else if (day == 8) {
      day_word = "eighth";
    }
    else if (day == 9) {
      day_word = "ninth";
    }
    else if (day == 10) {
      day_word = "tenth";
    }
    else if (day == 11) {
      day_word = "eleventh";
    }
    else if (day == 12) {
      day_word = "twelfth";
    }    
    else if (day == 13) {
      day_word = "thirteenth";
    }
    else if (day == 14) {
      day_word = "fourteenth";
    }
    else if (day == 15) {
      day_word = "fifteenth";
    }
    else if (day == 16) {
      day_word = "sixteenth";
    }
    else if (day == 17) {
      day_word = "seventeenth";
    }
    else if (day == 18) {
      day_word = "eighteenth";
    }
    else if (day == 19) {
      day_word = "nineteenth";
    }
    else if (day == 20) {
      day_word = "twentieth";
    }
    else if (day == 21) {
      day_word = "twenty-first";
    }
    else if (day == 22) {
      day_word = "twenty-second";
    }
    else if (day == 23) {
      day_word = "twenty-third";
    }
    else if (day == 24) {
      day_word = "twenty-fourth";
    }
    else if (day == 25) {
      day_word = "twenty-fifth";
    }
    else if (day == 26) {
      day_word = "twenty-sixth";
    }
    else if (day == 27) {
      day_word = "twenty-seventh";
    }
    else if (day == 28) {
      day_word = "twenty-eighth";
    }
    else if (day == 29) {
      day_word = "twenty-ninth";
    }
    else if (day == 30) {
      day_word = "thirtieth";
    }
    else if (day == 31) {
      day_word = "thirty-first";
    }

    System.out.println("Your birthday is: " + month_word + " " + day_word);
    System.out.println(horoscope);
  }
}