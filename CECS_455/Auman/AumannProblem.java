import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class AumannProblem {
	public ArrayList<HashSet<Integer>> aPartition=new ArrayList<HashSet<Integer>>();
	public ArrayList<HashSet<Integer>> bPartition=new ArrayList<HashSet<Integer>>();
	public HashMap<Integer,Pair<BigInteger,BigInteger>> distribution=new HashMap<Integer,Pair<BigInteger,BigInteger>>();
	public HashSet<Integer> E=new HashSet<Integer>();
	public int s=-1; // true state of the world
	
	public void initializeExample() {
		aPartition.clear();
		HashSet<Integer> temp=new HashSet<Integer>(); temp.add(1); temp.add(2); aPartition.add(temp);
		temp=new HashSet<Integer>(); temp.add(3); temp.add(4); aPartition.add(temp);
		temp=new HashSet<Integer>(); temp.add(5); aPartition.add(temp);
		
		bPartition.clear();
		temp=new HashSet<Integer>(); temp.add(1); bPartition.add(temp);
		temp=new HashSet<Integer>(); temp.add(2); bPartition.add(temp);
		temp=new HashSet<Integer>(); temp.add(3); temp.add(4); temp.add(5); bPartition.add(temp);
		
		distribution.clear();
		distribution.put(1, new Pair<BigInteger,BigInteger>(BigInteger.ONE,BigInteger.valueOf(7L)));
		distribution.put(2, new Pair<BigInteger,BigInteger>(BigInteger.valueOf(2L),BigInteger.valueOf(7L)));
		distribution.put(3, new Pair<BigInteger,BigInteger>(BigInteger.ONE,BigInteger.valueOf(7L)));
		distribution.put(4, new Pair<BigInteger,BigInteger>(BigInteger.valueOf(2L),BigInteger.valueOf(7L)));
		distribution.put(5, new Pair<BigInteger,BigInteger>(BigInteger.ONE,BigInteger.valueOf(7L)));
		
		E.clear();
		E.add(1); E.add(2); E.add(3);
		
		s=3;
	}
	
	public void printout() {
		// For student use.
		System.out.println("A partition: "+aPartition.toString());
		System.out.println("B partition: "+bPartition.toString());
		for (int key:distribution.keySet())
			System.out.println(""+key+": "+distribution.get(key).first.toString()+"/"+distribution.get(key).second.toString());
		System.out.println("E: "+E.toString());
		System.out.println("True state of the world: "+s);
	}
}
