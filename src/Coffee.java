public class Coffee extends Beverage {
    public Coffee (int num_cups) {
        super(num_cups);
    }
    public void AddPowder() {
        System.out.println("Add " + getCups() + " cups coffee powder");
    }
}