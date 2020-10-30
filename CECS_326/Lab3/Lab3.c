#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>






int main(int argc, char *argv[]){
	int[] arr = {7,12,19,3,18,4,2,6,15,8};
    int arr_size = sizeof(arr)/sizof(arr[0]);
    printf(arr_size);//array size is 10
    
	
	
    
    if(pthread_barrier_init(&barrier, NULL, thread_count)){//initialized to check if any thread is blocked
        printf("Barrier not created...");
        return -1;
    }

    pthread_t array[] = arr;//creating a unique data type for threads
    for(int i = 0; i < sizeof(array); i++){
        printf("%d ", array[i]);
    }
    // for(i = 0; i < thread_count; i++){
    //     pthread_create(&array[i], NULL, ThreadID,(void *)(long) i);//creates the threads
    // }
    // for ( i = 0; i < thread_count; i++){
    //     pthread_join(array[i], NULL);//waits for current thread to finish before calling the next one
    // }
		
		
	
	
	return 0;
}