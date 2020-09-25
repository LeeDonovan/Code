import java.util.*;

public class RunForYourLife{

    public static int seed(){
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter a seed value: ");
        return in.nextInt();
    }
/////////////////////////////Get Input Size///////////////////////////////////////////////////////////////////////////
    public static int value(){
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter a input size: ");
        return in.nextInt();
    }
/////////////////////////////////Create A random list////////////////////////////////////////////////////////////////////////
    public static int[] randomList(int n, int s){
        int randNumbers[];
        randNumbers = new int[n];
        Random rand = new Random(s);//seeded value
        int min = -100;
        int max = 101;
        for(int i = 0; i<n; i++){
            int randNumeral = rand.nextInt(max - min) + min;
            randNumbers[i] = randNumeral;
        }
        return randNumbers;
    }
//////////////////////////////////Fred's Algorithm//////////////////////////////////////////////////////////////////////
    public static int Fred(int[] x){
        int max = 0;
        for (int i = 0; i <x.length; i++ ){
            for(int j = i; j < x.length; j++){
                int thisSum = 0;
                for (int k = i; k<j + 1;k++){
                    thisSum = thisSum +  x[k];
                }
                if(thisSum > max){
                    max = thisSum;
                }
            }
        }
        return max;
    }
//////////////////////////////////////Sophie's Algorithm///////////////////////////////////////////////////////////////////////////
    public static int Sophie(int[] x){
        int max = 0;
        for(int i = 0; i < x.length; i ++){
            int thisSum = 0;
            for( int j = i; j < x.length; j++) {
                thisSum = thisSum + x[j];
                if(thisSum > max){
                    max = thisSum;
                }
            }
        }
        return max;
    }
///////////////////////////////////////Johnny's Algorithm///////////////////////////////////////////////////////////////////////////////////
    public static int Johnny(int[] x, int left, int right){
        if(x.length == 0){
            return 0;
        }
        else if(left == right){
            if(x[left] > 0) {
                return x[left];
            }
            return 0;
        }
        int center = (left + right) /2;
        int maxLeftSum = Johnny(x, left, center);
        int maxRightSum = Johnny(x, center + 1, right);

        int maxLeftBorder = 0;
        int leftBorder = 0;
        for (int i = center; i >= left; i--){
            leftBorder += x[i];
            if(leftBorder > maxLeftBorder){
                maxLeftBorder = leftBorder;
            }
        }

        int maxRightBorder = 0;
        int rightBorder = 0;
        for (int j = center + 1; j <= right; j++){
            rightBorder += x[j];
            if(rightBorder > maxRightBorder){
                maxRightBorder = rightBorder;
            }
        }
        return Math.max(Math.max(maxLeftSum, maxRightSum), maxLeftBorder + maxRightBorder);

    }
////////////////////////////////Sally's Algorithm//////////////////////////////////////////////////////////////////////////
    public static int Sally(int[] x){
        int max = 0;
        int thisSum = 0;
        for (int i = 0; i < x.length; i ++){
            thisSum += x[i];
            if(thisSum > max){
                max = thisSum;
            }
            else if (thisSum < 0){
                thisSum = 0;
            }
        }
        
        return max;
    }
/////////////////////////////Test Function/////////////////////////////////////////////////////////////////////////
    public static void testing(int[] x){
        long startTime = System.currentTimeMillis();
        System.out.println("Freddy's Algorithm: " + Fred(x));
        long endTime = System.currentTimeMillis();
        long totalTime = endTime - startTime;
        System.out.println("Freddy's Time: "+ totalTime + " ms\n");

        startTime = System.currentTimeMillis();
        System.out.println("Sophie's Algorithm: " + Sophie(x));
        endTime = System.currentTimeMillis();
        totalTime = endTime - startTime;
        System.out.println("Sophie's Time: "+ totalTime + " ms\n");
        
        startTime = System.currentTimeMillis();
        System.out.println("Johnny's Algorithm: " + Johnny(x, 0, x.length - 1));
        endTime = System.currentTimeMillis();
        totalTime = endTime - startTime;
        System.out.println("Johnny's Time: "+ totalTime + " ms\n");

        
        startTime = System.currentTimeMillis();
        System.out.println("Sally's Algorithm: " + Sally(x));
        endTime = System.currentTimeMillis();
        totalTime = endTime - startTime;
        System.out.println("Sally's Time: "+ totalTime + " ms\n");

    }
///////////////////////////////////Main/////////////////////////////////////////////////////////////////////////////////
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        boolean loop = true;
        while(loop){

            System.out.println("_________________________________");
            System.out.println("1. Quit The Program");
            System.out.println("2. Time Freddy's algorithm");
            System.out.println("3. Time Sophie's algorithm");
            System.out.println("4. Time Johnny's algorithm");
            System.out.println("5. Time Sally's algorithm");
            System.out.println("6. Test the Algorithms");
            System.out.println("Choose a menu: ");
            
            int userInput = in.nextInt();
////////////////////////////////////////////////////////////////////////////////////////////////////////
            if(userInput == 1){//Quit Program
                loop = false;
            }
///////////////////////////////////////////////////////////////////////////////////////////////////////////
            if(userInput == 2){
                System.out.println("\nWelcome To Freddy's Algorithm");
                int s = seed();
                int n = value();
                int[] randomNumbers =  randomList(n,s);
                double startTime = System.currentTimeMillis();
                int FreddyAlgo = Fred(randomNumbers);
                double endTime = System.currentTimeMillis();
                double totalTime = endTime - startTime;
                System.out.println("Freddy's Outcome: " + FreddyAlgo);
                System.out.println("Freddy's Time: "+ totalTime + " ms\n");

            }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if(userInput == 3){
                System.out.println("\nWelcome To Sophie's Algorithm");
                int s = seed();
                int n = value();
                int randomNumbers[] =  randomList(n,s);
                double startTime = System.currentTimeMillis();
                int SophieAlgo = Sophie(randomNumbers);
                double endTime = System.currentTimeMillis();
                double totalTime = endTime - startTime;
                System.out.println("Sopie's Outcome: " + SophieAlgo);
                System.out.println("Sophie's Time: "+ totalTime + " ms\n");
            }
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if(userInput == 4){
                System.out.println("\nWelcome To Johnny's Algorithm");
                int s = seed();
                int n = value();
                int randomNumbers[] =  randomList(n,s);
                double startTime = System.currentTimeMillis();
                int JohnnyAlgo = Johnny(randomNumbers,0,randomNumbers.length-1);
                double endTime = System.currentTimeMillis();
                double totalTime = endTime - startTime;
                System.out.println("Johnny's Outcome: " + JohnnyAlgo);
                System.out.println("Johnny's Time: "+ totalTime + " ms\n");
            }
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if(userInput == 5){
                System.out.println("\nWelcome To Sally's Algorithm");
                int s = seed();
                int n = value();
                int[] randomNumbers =  randomList(n,s);
                double startTime = System.currentTimeMillis();
                int SallyAlgo = Sally(randomNumbers);
                double endTime = System.currentTimeMillis();
                double totalTime = endTime - startTime;
                System.out.println("Sally's Outcome: " + SallyAlgo);
                System.out.println("Sally's Time: "+ totalTime + " ms\n");
            }
///////////////////////Testing Algorithms////////////////////////////////////////////////////////////////////////
            if(userInput == 6){
                boolean testing = true;
                while (testing){
                    System.out.println("1. Array of 10 values +/-");
                    System.out.println("2. Array of 11 values +/-");
                    System.out.println("3. Array of no values");
                    System.out.println("4. Array of 10 values -");
                    System.out.println("5. Array of 10 values of 0s");
                    System.out.println("6. Array of 10 values +");
                    System.out.println("7. Leave Testing");
                    System.out.println("Choose menu: ");
                    int tester = in.nextInt();

                    if(tester == 1){
                        System.out.println("Testing 10 values of +/-");
                        int[] x = {1,-10,5,67,-45,-90,40,12,-54,32};
                        testing(x);
                    }
                    if(tester == 2){
                        System.out.println("Testing 11 values of +/-");
                        int[] x = {1,-10,5,67,-45,-90,40,12,-54,32,21};
                        testing(x);
                    }

                    if(tester == 3){
                        System.out.println("Testing 0 values");
                        int[] x = {};
                        testing(x);
                    }

                    if(tester == 4){
                        System.out.println("Testing 10 values of -");
                        int[] x = {-1,-10,-5,-67,-45,-90,-40,-12,-54,-32};
                        testing(x);
                    }

                    if(tester == 5){
                        System.out.println("Testing 10 values of +/-");
                        int[] x = {0,0,0,0,0,0,0,0,0,0};
                        testing(x);
                    }

                    if(tester == 6){
                        System.out.println("Testing 10 values of +/-");
                        int[] x = {1,10,5,67,45,90,40,12,54,32};
                        testing(x);
                    }
                    if(tester == 7){
                        testing = false;
                    }
                    



                }
            }

        }
        
    }
    
}