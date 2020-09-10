/*
Donovan Lee
CECS_455
Lab 1: Space Invaders
9/10/2020
*/

import java.util.*;


public class StudentSolver{

    public static HashSet<Integer> solve(HashMap<Integer, Integer> aliens){
        double sum = 0;
        int magicNum = 1 ; // ? 
        int counter = 0;
        int adder = 0;
        Iterator traverse = aliens.entrySet().iterator();// go thru Hashmap
        HashSet<Integer> all = new HashSet<Integer>();
        while(traverse.hasNext()){
            counter++;
            Map.Entry alienSet = (Map.Entry)traverse.next();// goes thru hashmap
            System.out.println(alienSet);
            int alienID = (int)alienSet.getKey();
            System.out.println("Alien ID: " + alienID);
            sum += (Math.pow(2,-aliens.get(alienID)));//get alien's level from beginning
            if(sum >= magicNum){
                break;
            }
        }

        System.out.println("Counter: " + counter);
        while (adder != counter){
            int keys = (int)aliens.keySet().toArray()[adder];
            System.out.println("Key = "+ keys);
            all.add(keys);
            adder ++;
        }
        
        return all;
    }


    public static void main(String args[]){

        HashMap<Integer,Integer> aliens = new HashMap<Integer,Integer>();
        aliens.put(1, 3);
        aliens.put(2, 1);
        aliens.put(3, 2);
        aliens.put(4, 3);
        aliens.put(5, 3);
        aliens.put(6, 2);
        HashSet<Integer> totalAliens = new HashSet<Integer>();
        totalAliens = solve(aliens);
        System.out.println("Aliens: " + totalAliens);
        

        
    }



}