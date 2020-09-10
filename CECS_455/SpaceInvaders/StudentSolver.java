/*
Donovan Lee: 016741645
CECS_455
Lab 1: Space Invaders
9/10/2020
*/

import java.util.*;

public class StudentSolver{

    public static HashSet<Integer> solve(HashMap<Integer, Integer> aliens){
        double sum = 0;
        double magicNum = 0.2; // ? 
        int counter = 0;
        int adder = 0;
        Iterator traverse = aliens.entrySet().iterator();// go thru Hashmap
        HashSet<Integer> all = new HashSet<Integer>();
        if(aliens.isEmpty()){//checks for empty hashmap
            return all;
        }
        else{
            while(traverse.hasNext()){
                Map.Entry alienSet = (Map.Entry)traverse.next();// goes thru hashmap
                System.out.println(alienSet);
                int alienID = (int)alienSet.getKey();
                sum += (Math.pow(2,-aliens.get(alienID)));//get alien's level from beginning
                counter++;
                if(sum >= magicNum){
                    break;
                }
            }
            while (adder != counter){
                int keys = (int)aliens.keySet().toArray()[adder];
                all.add(keys);
                adder ++;
            }
        }
        
        
        return all;
    }
}