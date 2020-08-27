import java.util.*;

public class StudentSolver{

    public static HashSet<Integer> solve(HashMap<Integer, Integer> aliens){
        int counter = 0;
        for(int i = 0; i < aliens.size(); i++){
            counter+=aliens.get(i);
        }
        HashSet<Integer> all = new HashSet<Integer>();
        all.add(counter);
        return all;
    }


    public static void main(String args[]){

        Scanner input = new Scanner(System.in);
        HashMap<Integer,Integer> aliens = new HashMap<Integer,Integer>();
        System.out.println("Please enter a number: ");
        int counter = input.nextInt(); //gets the number of aliens you want
        while(counter > 0){
            aliens.put(counter, counter); //adds in number of aliens into hashmap
            counter--;
        }
        HashSet<Integer> total = new HashSet<Integer>();
        total = solve(aliens);
        System.out.println(total);

        
    }



}