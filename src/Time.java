class Time {

    private int hour;
    private int minutes;
    public Time () {
        hour = 12;
        minutes = 0;
    }
    public Time (int h, int m) {
        if (h >= 1 && h <= 23) {
            hour = h;
        } 
        if (m >= 0 && m <= 59) {
            minutes = m;
        }   
    }
    public String toString () {
        String formatted_hour = Integer.toString(hour);
        String formatted_minutes = Integer.toString(minutes);
        if (hour < 10) {
            formatted_hour = "0" + hour;
        }
        if (minutes < 10) {
            formatted_minutes = "0" + minutes;
        }
        return formatted_hour + formatted_minutes;
    }
    public String convert () {
       String formatted_minutes = "" + minutes;
       if (minutes < 10) {
           formatted_minutes = "0" + minutes;
       }
       if (hour < 12 && hour != 0) {
           return "" + hour + ":" + formatted_minutes + " am";
       } else if (hour > 12) {
           return "" + Math.abs(12 - hour) + ":" + formatted_minutes + " pm";
       } else if (hour == 12) {
           return "12:" + formatted_minutes + " pm";
       } else {
           return "12:" + formatted_minutes + " am";
       }
    }
    public void increment () {
        if (minutes == 59 && hour != 23) {
            minutes = 0;
            hour++;

        } else if (minutes == 59 && hour == 23) {
            minutes = 0;
            hour = 0;
        } else {
            minutes++;
        }
    }
}

