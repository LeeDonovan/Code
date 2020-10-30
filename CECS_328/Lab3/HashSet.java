import java.lang.reflect.Array;
import java.math.*;
import java.util.Objects;
// Implements the Map ADT using a hash table with separate chaining.
public class HashSet<T> {
    private class Entry {
        public T mKey;
        public boolean mIsNil;
        public Entry(T key, boolean Nil){
            this.mKey = key;
            this.mIsNil = Nil;
        }
    }

    private Entry[] mTable;
    private int mCount; // the number of elements in the set, i.e., "n"

    // Constructs a hashtable with the given size.
   public void HashMap(int tableSize) {
      // TODO: you must round up tableSize to the next power of 2!!!
        int power = 1;
        while(power < tableSize){
            power *=2;
        }
      // The next line is a workaround for Java not liking us making an array
      // of a generic type. (Node is a generic type because it has generic
      // members.)
      mTable = (Entry[])Array.newInstance(Entry.class, power); 
      
      // mTable's entries are all null initially.
      // mTable[i] == null ---> nothing has ever lived at index i
      // mTable[i] != null && mTable[i].mIsNil ---> something used to be here but was removed.
   }

   public void getmTable(){
        System.out.println(mTable.length);
   }

   public int index(T key){///get hashcode
        int num = Math.abs(key.hashCode());
        return num;
    }

    public void tableDouble(){//double to size
        int size = 2 * mTable.length;
        Entry[] temp = mTable;
        HashMap(size);
        mCount = 0;
        for(int i = 0; i < temp.length; i++){
            if(temp[i] != null ){
                add(temp[i].mKey);
            }
        }

    }
    public int getNums(){
        return mCount;
    }

    public int probFunc(int i){
        return (int) ((Math.pow(i,2)) + i)/2;
    }
    // Inserts the given key and value into the table, assuming no entry with
    // an equal key is present. If such an entry is present, override the entry's
    // value.

    public void add(T key) {
        if((double) mCount / mTable.length >= 0.8){
            tableDouble();
        } 
        int num = index(key);//hashcode

        for(int i = 0; i < mTable.length; i++){
            int probe = (num + probFunc(i)) % mTable.length;
            if(mTable[probe] == null){
                mTable[probe] = new Entry(key, false);
                mCount++;
                return;
            }
            else if(mTable[probe].mKey.equals(key)){
                return;
            }
        }

    }

    // Returns true if the given key is present in the set.
    public boolean find(T key) {
        int locate = index(key);
        for(int i = 0; i < mTable.length; i++){//loops through 
            int probe = (locate + probFunc(i)) % mTable.length;//probe function
            if(mTable[probe].mKey.equals(key)){
                return true;
            }

        }
        return false;
    }

    // Removes the given key from the set.
    public void remove(T key) {
        int bye = index(key);
        for(int i = 0; i < mTable.length; i++){//loops through 
            int probe = (bye + probFunc(i)) % mTable.length;//probe function
            if(mTable[probe].mKey.equals(key)){
                mTable[probe].mKey = null;
                mTable[probe].mIsNil = true;
                mCount--;
            }
        }
        // Use the hash code and probing function to keep looking for this key until:
        // 1. you find a null element
        // 2. you find the key
        // 3. you fail n times.

        // TODO: finish this method.
    }

}