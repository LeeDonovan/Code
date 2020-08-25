import java.util.*;

public class StudentSolver{

    //public static HashSet<Integer> solve(HashMap<Integer, Integer> aliens){

    //}


    public static void main(String args[]){

        Scanner input = new Scanner(System.in);
        HashMap<Integer,Integer> aliens = new HashMap<Integer,Integer>();
        System.out.println("Please enter a number: ");
        int counter = input.nextInt(); //gets the number of aliens you want
        while(counter > 0){
            aliens.put(counter, counter); //adds in number of aliens into hashmap
            counter--;
        }
        System.out.println(aliens);

        
    }



}