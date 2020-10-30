import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.lang.*;

public class EagleOne {
    public static void main(String[] args) {
        try{
            File text = new File("trump_speech.txt");
            Scanner in = new Scanner(text);
            HashSet<Object> unique = new HashSet<>();
            unique.HashMap(50);
            String words = in.nextLine();
            String lines[] = words.split("\\s+");
            Pattern checker = Pattern.compile("[^A-Za-z0-9]", Pattern.CASE_INSENSITIVE);
            for(int i = 0; i < lines.length; i ++){
                Matcher found = checker.matcher(lines[i]);
                if(found.find()){
                    lines[i] = lines[i].replaceAll("[^A-Za-z0-9]", "");
                }
                if(!lines[i].isEmpty()){
                    unique.add(lines[i]);
                }
                
            }
            System.out.println("There are " + unique.getNums() + " unique words.");
            in.close();
            if(unique.find("in")){
                System.out.println("It works?");
            }

        }
            catch(FileNotFoundException e){
                System.out.println("error: ");
                e.printStackTrace();
            }
            
            
        }
           
}
