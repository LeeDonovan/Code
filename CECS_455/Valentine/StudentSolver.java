import java.util.*;
import java.math.*;

public class StudentSolver{

    public static ArrayList<Boolean> solve(ArrayList<ArrayList<BigInteger>> problems){
        ArrayList<Boolean> win = new ArrayList<Boolean>();
        int size = problems.size();
        System.out.println("Arraylist size: " + size);//Check size
        for(int i = 0; i <size; i++ ){
            if(problems.get(i).size() == 0 || problems.get(i).size() % 2 == 0){
                win.add(true);
            }
            else{
                win.add(false);
            }
        }
        return win;
    }

}