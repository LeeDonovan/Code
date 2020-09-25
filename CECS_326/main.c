#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

int sharedVariable = 0;
pthread_mutex_t lock;
pthread_barrier_t barrier;

void SimpleThread(int which){
	int num, val;
	for(num = 0; num < 20; num++){
		if(random() > RAND_MAX/2){
			usleep(500);
		}
	
	#ifdef PTHREAD_SYNC
		pthread_mutex_lock(&lock);
	#endif
		val = sharedVariable;
		printf("***thread%d sees value %d\n", which,val);
		sharedVariable= val + 1;
	#ifdef PTHREAD_SYNC
		pthread_mutex_unlock(&lock);
	#endif
	}
	#ifdef PTHREAD_SYNC
		pthread_barrier_wait(&barrier);
	#endif
	val = sharedVariable;
	printf("Thread%d sees final value %d\n", which, val);
}

void *ThreadID(void * arg){
	int thread_id =(long) arg;
	SimpleThread(thread_id);
}

int main(int argc, char *argv[]){
	int i;
	int thread_count;
	
	if(argc != 2){//checks to see if only one parameter was taken
		printf("Please enter only one parameter for the command line");
		return(0);
	}
	else{
		thread_count = atoi(argv[1]);//converts string to int
		if(thread_count < 1){//checks to see if a positive number was inputted
			printf("Enter a positive whole number...");
			return 0;
		}
		
		if(pthread_barrier_init(&barrier, NULL, thread_count)){
			printf("Barrier not created...");
			return -1;
		}

		pthread_t array[thread_count];//creating a unique data type for threads

		for(i = 0; i < thread_count; i++){
			pthread_create(&array[i], NULL, ThreadID,(void *)(long) i);//creates the threads
		}
		for ( i = 0; i < thread_count; i++){
			pthread_join(array[i], NULL);//waits for current thread to finish before calling the next one
		}
		
		
	}
	
	return 0;
}
