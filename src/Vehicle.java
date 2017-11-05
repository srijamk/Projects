class Vehicle {
    private int location;
    
    public Vehicle () {
        location = 0;
    }
    public Vehicle (int loc) {
        if (loc >= -20 && loc <= 20) {
            location = loc;
        } else {
            location = 0;
        }
    }
    public void forward () {
        if (location < 20) {
            location++;
        }
    }
    
    public void backward () {
        if (location > -20) {
            location--;
        }
    }
    
    public int getLocation () {
        return location;
    }
    
    public String toString () {
        String location_string = "";
        for (int i = 1; i <= (location + 20); i++) {
            location_string += " "; 
        }
        location_string += "@";
        return location_string;
    }
}