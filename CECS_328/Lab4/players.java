import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.lang.*;

public class players {
    public static void main(String[] args) {
        try{
            RedBlackTreeMap<String, Integer> players = new RedBlackTreeMap<String, Integer>();
            File text = new File("players_homeruns.csv");
            Scanner in = new Scanner(new BufferedReader(new FileReader(text)));
            int count =0;
            while(in.hasNextLine()){
                String word = in.nextLine();
                String[] arr = word.split(",",2);
                String name = arr[0];
                int runs = Integer.parseInt(arr[1]);
                //System.out.println(i + ". "+ arr[0] + " "+ runs);
                players.add(name, runs);
                count++;
            }
            System.out.println("There are " + count + " players.");
            System.out.println("Finished adding to tree...");
            players.printStructure();
            System.out.println("Finished Printing Tree");
            System.out.println();
            if(players.find("Hank Aaron") == 755){
                System.out.println("First Condition on checking that Hank Aaron is a leaf with 2 NIL child...");
                if(players.checkNILs("Hank Aaron")){
                    System.out.println("Hank Aaron does have 2 NIL child");
                }
                else{
                    System.out.println("Key does not have 2 NIL child");
                }
            }
            System.out.println();
            if(players.find("Honus Wagner") == 101){
                System.out.println("Second Condition on checking Honus Wagner that is a root...");
                if(players.getKey().equals("Honus Wagner")){
                    System.out.println("Honus Wagner is the root!");
                }
                else{
                    System.out.println("Honus Wagner is not the root!");
                }
            }
            System.out.println();
            if(players.find("Babe Ruth") == 714){
                System.out.println("Third Condition on checking Babe Ruth that has one NIL and one non - NIL...");
                if(players.halfNHalf("Babe Ruth")){
                    System.out.println("Babe Ruth does have 1 NIL-child and 1 non-NIL child!");
                }
                else{
                    System.out.println("Babe Ruth does not have 1 NIL-child and 1 non-NIL child!");
                }
            }
            System.out.println();
            if(players.find("Ty Cobb") == 117){
                System.out.println("Fourth COndition on checking if Ty Cobb is in a red node...");
                if(players.reddyOrNot("Ty Cobb")){
                    System.out.println("Ty Cobbis in a red node!");
                }
                else{
                    System.out.println("Ty Cobb is not in a red node");
                }
            }
            System.out.println();
            System.out.println("Total key count: " + players.getCount());
            in.close();
        }
        catch(FileNotFoundException e){
            System.out.println("error: ");
            e.printStackTrace();
        }
        
    }
}
