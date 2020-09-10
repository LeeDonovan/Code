import java.util.*;

public class test {

    public static void main(String args[]){
        HashMap<Integer,Integer> aliens = new HashMap<Integer,Integer>();
        aliens.put(4, 2);
        aliens.put(5, 1);
        aliens.put(6, 2);
        Iterator traverse = aliens.entrySet().iterator();
        while (traverse.hasNext()) { 
            Map.Entry mapElement = (Map.Entry)traverse.next(); 
            int marks = ((int)mapElement.getValue()); 
            System.out.println(mapElement.getKey() + " : " + marks); 
        } 
        System.out.println(aliens.entrySet());
        System.out.println(aliens.get(aliens.keySet()));
        sum += (Math.pow(2,-aliens.get(increase)));
    }
}

if( n > 0 ){
    for(int i = 0; i < n; i++){
        counter++;
        sum += (Math.pow(2,-aliens.get(increase)));
        System.out.println("Sum = " +sum);
        
        if(sum >= magicNum ){
            break; 
        }
        increase++;
    }
}