import java.util.*;

public class test {

    public static void main(String args[]){
        HashMap<Integer, Integer> aliens = new HashMap<Integer,Integer>();
        HashSet<Integer> totalAliens = new HashSet<Integer>();
        int number = 2000;
        int min = 1;
        int max = 20;
        int counter = 1;
        while (counter != number){
            int randNumeral = ThreadLocalRandom.current().nextInt(min, max +1);
            aliens.put(counter, randNumeral);
            counter++;

        }
        System.out.println(aliens);
        totalAliens = solve(aliens);
        System.out.println("Alien set: " + totalAliens);
        


    }


    if(x.length == 0){
        return 0;
    }
    else if(left == right){
        if(x[left] > 0) {
            return x[left];
        }
        return 0;
    }