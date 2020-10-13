public class Tester {
    public static ArrayList<Boolean> solve(ArrayList<ArrayList<BigInteger>> problems){
        ArrayList<Boolean> win = new ArrayList<Boolean>();
        int size = problems.size();
        System.out.println("Arraylist size: " + size);//Check size
        for(int i = 0; i <size; i++){//go into arraylist
            System.out.println(i + " loop");
            int binSum = 0;
            for(int j = 0; j < problems.get(i).size(); j++){//grab the first arraylist for bigints
                String temp = problems.get(i).get(j).toString(2);//converted to a string binary
                System.out.println("Converted to Binary? " + temp + "Type: " + temp.getClass().getSimpleName());
                int temp2 = temp.intValue();
                System.out.println("Converted to Integer? " + temp2 + "Type: " + temp.getClass().getSimpleName());
                binSum  = binSum + temp2;
                System.out.println("Did it add correctly? " + binSum + "Type: " + temp.getClass().getSimpleName());
            }
            if(binSum >= 4){
                win.add(true);
            }
            else{
                win.add(false);
            }
            
        }
        return win;
    }



    public static void main(String[] args) {
        ArrayList<BigInteger> chocolate = new ArrayList<BigInteger>();// chocolate BigInts 
        ArrayList<BigInteger> chocolate1 = new ArrayList<BigInteger>();// chocolate BigInts 
        ArrayList<BigInteger> chocolate2 = new ArrayList<BigInteger>();// chocolate BigInts 
        BigInteger a = new BigInteger("10000000");
        BigInteger b = new BigInteger("12321");
        BigInteger c = new BigInteger("10000123213000");
        BigInteger d = new BigInteger("10000001230");
        BigInteger e = new BigInteger("1231232");
        ArrayList<ArrayList<BigInteger>> games = new ArrayList<ArrayList<BigInteger>>();//Holds arraylist of choco 
        ArrayList<Boolean> winner = new ArrayList<Boolean>();
        chocolate.add(a);
        chocolate.add(b);
        chocolate.add(c);
        chocolate.add(d);
        chocolate.add(e);

        chocolate1.add(a);
        chocolate1.add(b);
        chocolate1.add(c);
        chocolate1.add(d);

        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);
        chocolate2.add(a);

        

        games.add(chocolate);
        games.add(chocolate1);
        games.add(chocolate2);
        winner = solve(games);
        System.out.println(winner);
    }
}
