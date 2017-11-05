public abstract class Beverage 
{
    private int numcups;
    public Beverage (int num_cups) {
        numcups = num_cups;
    }
    public int getCups() {
        return numcups;
    }
    public void Make(){
       System.out.println("Heat the milk");
       System.out.println("Add sugar");
       AddPowder();
       System.out.println("Boil for 30 mins");
       System.out.println("Serve");
    }
    public abstract void AddPowder();
}
