public class Tea extends Beverage {
    public Tea (int num_cups) {
        super(num_cups);
    }
    public void AddPowder() {
        System.out.println("Add " + getCups() + " tea bag contents");
    }
}