class CarPrices {
    private int prices [][] = new int [3][4];
    public CarPrices () {
        for (int i = 0; i < prices.length; i++) {
            for (int j = 0; j < prices[i].length; j++) {
                prices[i][j] = 50000;
            }
        }
    }
    public CarPrices(int model, int price) {
        for (int i = 0; i < prices.length; i++) {
            for (int j = 0; j < prices[i].length; j++) {
                if (i == model) {
                    prices[i][j] = price;
                } else {
                    prices[i][j] = 50000;
                }
            }
        }        
    }
    public void getPrices () {
        for (int i = 0; i < prices.length; i++) {
            for (int j = 0; j < prices[i].length; j++) {
                System.out.print(prices[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main (String [] args) {
        CarPrices Toyota = new CarPrices(1, 30000);
        CarPrices Audi = new CarPrices();
        CarPrices Hyundai = new CarPrices(2, 100000);
        Toyota.getPrices();
        Audi.getPrices();
        Hyundai.getPrices();
    }
}