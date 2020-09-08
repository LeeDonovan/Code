import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class RunForYourLife{


    public static ArrayList<Integer> values(){
        ArrayList<Integer> user = new ArrayList<Integer>();
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter a seed value: ");
        int seed = in.nextInt();
        System.out.println("\nPlease enter an input size: ");
        int size = in.nextInt();
        user.add(seed);
        user.add(size);
        return user;

    }

    public static ArrayList<Integer> randomList(int n){
        Random rand = new Random();
        ArrayList<Integer> randNumbers = new ArrayList<Integer>();
        int counter = 0;
        int min = -100;
        int max = 100;
        while(counter != n){
            int randNumeral = ThreadLocalRandom.current().nextInt(min, max +1);
            System.out.println(randNumeral);
            randNumbers.add(randNumeral);
            counter++;
        }
        return randNumbers;
    }

    public static void FreddysAlgo (ArrayList<Integer> x){
        int max = 0;
        for (int i = 0; i <x.size(); i++ ){
            for(int j = i; j < x.size(); j++){
                int thisSum = 0;
                for (int k = i; k<j;k++){
                    thisSum += x.get(k);
                    System.out.println("The sum is: " +thisSum);
                }
                if(thisSum > max){
                    max = thisSum;
                    System.out.println("The new max is " + max);
                }
            }
        }
        System.out.println(max);
    }

    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        boolean loop = true;
        while(loop){
            System.out.println("1. Quit The Program");
            System.out.println("2. Time Freddy's algorithm");
            System.out.println("3. Time Sophie's algorithm");
            System.out.println("4. Time Johnny's algorithm");
            System.out.println("5. Time Sally's algorithm");
            System.out.println("Choose a menu: ");
            int userInput = in.nextInt();
            if(userInput == 1){
                loop = false;
            }
            if(userInput == 2){
                System.out.println("Welcome To Freddy's Algorithm");
                ArrayList<Integer> fred = new ArrayList<Integer>();
                ArrayList<Integer> randomNumbers = new ArrayList<Integer>();
                fred = values();
                int s = fred.get(0);
                int n = fred.get(1);
                randomNumbers =  randomList(n);
                FreddysAlgo(randomNumbers);
                

                
            }
            if(userInput == 3){
                loop = false;
            }
            if(userInput == 4){
                loop = false;
            }
            if(userInput == 5){
                loop = false;
            }

        }
        
    }
    
}