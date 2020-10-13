import java.util.*;

public class OutOfSorts{
////////// Sorted List /////////////////////////////////////////////////////
    public static int[] sortedList(){
        int sortedNums[] = new int[100000];
        for(int i = 0; i < 100000; i++){
            sortedNums[i] = i + 1;
        }
        return sortedNums;
    }
///////////// Reverse List /////////////////////////////////////////////////////////
    public static int[] reverseSorted(){
        int sortedNums[] = new int[100000];
        int max = 100000;
        for(int i = 0; i< 100000; i ++){
            sortedNums[i] = max;
            max--;
        }
        return sortedNums;
    }
///////// Random List /////////////////////////////////////////////////////
    public static int[] randomSort(){
        int randNumbers[] = new int[100000];
        for(int i = 0; i<100000; i++){
            randNumbers[i] = (int)(Math.random() * 100000) + 1;
        }
        return randNumbers;
    }
//////// Insertion Sort //////////////////////////////////////////
public static boolean isOrdered(int[] x){
    for (int i = 1; i < x.length; i++){
        if(x[i-1] > x[i]){
            return false;
        }
    }
    return true;
}
/////// Insertion Sort ///////////////////////////////////////////
public static void insertionSort(int x[]){
    int n = x.length;
    for(int i = 1; i < n; i++){
        int j = x[i];
        int temp = x[i];
        for(j = i-1; j >= 0; j--){
            if(x[j] > temp){
                x[j + 1] = x[j];
            }
            else{
                break;
            }
        }
        x[j+1] = temp;
    }
}
///////////// Quick Sort //////////////////////////////////////////
public static void quickSort(int x[], int start, int end){
    if(end - start <= 10){
        insertionSort(x);
    }
    else{
        int median = medianOfThree(x, start , end);
        int split = partition(x , start, end, median);
        
        quickSort(x, start, split-1 );

        quickSort(x, split + 1, end );

    } 
}
///////// Partition /////////////////////////////
public static int partition(int x[], int left, int right, int pivotIndex){
    int pivotValue = x[pivotIndex];
    
    swap(x,pivotIndex, right );
    int store = left;//next position
    for(int i = left; i < right; i++){
        if(x[i] <= pivotValue){
            swap(x, store, i);
            store++;
        }
    }
    swap(x, right, store);
    return store;
}
///////////////// Median Of Three //////////////////////////////////////////////
public static int medianOfThree(int x[], int left, int right){
    int center = (left + right)/2;
    if(x[left] > x[center]){
        if(x[center] > x[right]){
            return center;
        }
        else if(x[left] > x[right]){
            return right;
        }
        else{
            return left;
        }
    }
    else{
        if(x[left] > x[right]){
            return left;
        }
        else if(x[center] > x[right]){
            return right;
        }
        else{
            return center;
        }
    }
}
public static void swap(int a[], int x, int y){
    int temp = a[x];
    a[x] = a[y];
    a[y] = temp;
}

/////////////// Main ///////////////////////////////////////////////
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean loop = true;
        while(loop){

            System.out.println("_________________________________");
            System.out.println("1. Quit The Program");
            System.out.println("2. Sorted");
            System.out.println("3. Random");
            System.out.println("4. Reverse");
            System.out.println("Choose a menu: ");
            
            int userInput = in.nextInt();

            if(userInput == 1){//Quit Program
                System.out.println("Exiting program...");
                loop = false;
            }
////////////////////// Sorted ////////////////////////////////////////////////
            if(userInput == 2){//Sorted
                int original[] = sortedList(); 
                int duplicate[] = original.clone();
                ///// Insertion Sort Time ////////////
                long startTime = System.nanoTime();

                insertionSort(duplicate);

                long endTime = System.nanoTime();
                long totalTime = endTime - startTime;
                System.out.println("Insertion Time for Sorted: "+ totalTime + " ns\n");

                boolean sorted = isOrdered(duplicate);
                if(sorted){
                    System.out.println(sorted);
                }
                else{
                    System.out.println(sorted);
                }
                ///// Quick Sort Time //////////////
                int duplicate2[] = original.clone();
                startTime = System.currentTimeMillis();

                quickSort(duplicate2, 0 , duplicate2.length-1);

                endTime = System.currentTimeMillis();
                totalTime = endTime - startTime;
                System.out.println("Quick Time for Sorted: "+ totalTime + " ms\n");

                sorted = isOrdered(duplicate2);
                if(sorted){
                    System.out.println(sorted);
                }
                else{
                    System.out.println(sorted);
                }
            }
//////////// Random////////////////////////////////////////////////////            
            if(userInput == 3){//Random
                System.out.println("Random List...");
                int original[] = randomSort();
                int duplicate[] = original.clone(); 
                long startTime = System.currentTimeMillis();

                insertionSort(duplicate);

                long endTime = System.currentTimeMillis();
                long totalTime = endTime - startTime;
                System.out.println("Insertion Time for Random: "+ totalTime + " ms\n");

                boolean sorted = isOrdered(duplicate);
                if(sorted){
                    System.out.println(sorted);
                }
                else{
                    System.out.println(sorted);
                }

                int duplicate2[] = original.clone();
                startTime = System.currentTimeMillis();

                quickSort(duplicate2, 0 , duplicate2.length-1);

                endTime = System.currentTimeMillis();
                totalTime = endTime - startTime;
                System.out.println("Quick Time for Random: "+ totalTime + " ms\n");

                sorted = isOrdered(duplicate2);
                if(sorted){
                    System.out.println(sorted);
                }
                else{
                    System.out.println(sorted);
                }
            }
/////////////// Reverse ////////////////////////////////////////////////////////
            if(userInput == 4){//Reverse
                System.out.println("Reverse List...");
                int original[] = reverseSorted();
                int duplicate[] = original.clone();
                long startTime = System.currentTimeMillis();

                insertionSort(duplicate);

                long endTime = System.currentTimeMillis();
                long totalTime = endTime - startTime;
                System.out.println("Insertion Time for Random: "+ totalTime + " ms\n");

                boolean sorted = isOrdered(duplicate);
                if(sorted){
                    System.out.println(sorted);
                }
                else{
                    System.out.println(sorted);
                }

                int duplicate2[] = original.clone();
                startTime = System.currentTimeMillis();

                quickSort(duplicate2, 0 , duplicate2.length-1);

                endTime = System.currentTimeMillis();
                totalTime = endTime - startTime;
                System.out.println("Quick Time for Random: "+ totalTime + " ms\n");

                sorted = isOrdered(duplicate2);
                if(sorted){
                    System.out.println(sorted);
                }
                else{
                    System.out.println(sorted);
                }
            }
        } 
    }
}