

@SuppressWarnings("rawtypes")
public class Pair<T, S> implements Comparable {
	public T first;
	public S second;
	public Pair(T f, S s) { first = f; second = s; }
	public Pair() { first=null; second=null; }
	@Override
	public String toString() { return "(" + first.toString() + ", " + second.toString() + ")"; }
	@SuppressWarnings("unchecked")
	@Override
	public boolean equals(Object o) { 
		Pair<T,S> other=(Pair<T,S>)o;
		if (first.getClass().equals(Integer.class)&&second.getClass().equals(Integer.class))
			return ((((Integer)first).intValue()==((Integer)other.first).intValue())&&
					(((Integer)second).intValue()==((Integer)other.second).intValue()));
		return ((this.first.equals(other.first))&&(this.second.equals(other.second))); }
	@Override
	public int hashCode() {
		if (first.getClass().equals(Integer.class)&&second.getClass().equals(Integer.class))
			return ((Integer)first).intValue()<<16|(((Integer)second).intValue()&32767);
		else if (first.getClass().equals(String.class)&&second.getClass().equals(Integer.class))
			return ((String)first+","+(Integer)second).hashCode();
		else if (first.getClass().equals(String.class)) 
			return ((String)first+","+(String)second).hashCode(); 
		else return first.hashCode()+second.hashCode(); }
	@SuppressWarnings("unchecked")
	@Override
	public int compareTo(Object otherObject) {
		Pair<T,S> other=(Pair<T,S>) otherObject;
		if ((first.getClass().equals(Integer.class))&&(second.getClass().equals(Integer.class)))
			if (((Integer)first).intValue()!=((Integer)other.first).intValue())
				return (((Integer)first).intValue()-((Integer)other.first).intValue());
			else return (((Integer)second).intValue()-((Integer)other.second).intValue());
		throw new RuntimeException("Not implemented.");
	}
}
