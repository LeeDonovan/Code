import java.util.*;
import java.lang.Math;

public class StudentSolver{

    public static HashSet<Integer> solve(HashMap<Integer, Integer> aliens){
        double sum = 0;
        int n = aliens.size();
        int increase = 1;
        HashSet<Integer> all = new HashSet<Integer>();
        if( n > 0 ){
            for(int i = 0; i < n; i++){
                
                sum += (Math.pow(2,-aliens.get(increase)));//summation formula
                System.out.println(sum);
                if(increase != n ){
                    increase++;
                }
                
            }
        }
        
        System.out.println(sum);
        
        return all;
    }


    public static void main(String args[]){

        Scanner input = new Scanner(System.in);
        HashMap<Integer,Integer> aliens = new HashMap<Integer,Integer>();
        System.out.println("Please enter a number: ");
        int counter = input.nextInt(); //gets the number of aliens you want
        int hold = counter;
        System.out.println("Please enter a Levels: ");
        int level = input.nextInt();//gets the number of levels
        while(counter > 0 ){
            aliens.put(counter,level);
            counter--;
            if(counter % 5 == 0){
                level--;
            }
        }
        System.out.println(aliens + " " + aliens.size());
        HashSet<Integer> totalAliens = new HashSet<Integer>();
        totalAliens = solve(aliens);
        System.out.println(totalAliens);
        

        
    }



}