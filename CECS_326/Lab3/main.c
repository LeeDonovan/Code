#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

pthread_mutex_t lock;
pthread_barrier_t barrier;
int arr[] = {7,12,19,3,18,4,2,6,15,8};
int arr_size = sizeof(arr)/sizeof(arr[0]);
int first[5];
int half[5];
int sort[10];
int counter = 0;

void *SortArrays(void *x);
void *fullSort(void *x);

void *fullSort(void *x){
	int *num = (int *)x;
	for(int i = 0; i <arr_size; i++){
		int j = num[i];
		int temp = num[i];
		for(j = i-1; j>=0;j--){
			if(num[j] > temp){
				num[j + 1] = num[j];
			}
			else{
				break;
			}
		}
		num[j+1] = temp;
	}	
}


void *SortArrays(void *x){
	int *num = (int *)x;
	for(int i = 0; i <arr_size/2; i++){
		int j = num[i];
		int temp = num[i];
		for(j = i-1; j>=0;j--){
			if(num[j] > temp){
				num[j + 1] = num[j];
			}
			else{
				break;
			}
		}
		num[j+1] = temp;
	}	
}



int main(){

	int half_size = arr_size/2;
	if(pthread_barrier_init(&barrier, NULL, arr_size)){//initialized to check if any thread is blocked
        printf("Barrier not created...");
        return -1;
    }
    	printf("First half of array unsorted\n");
	for(int i = 0; i < arr_size/2; i++){
		first[i] = arr[i];
		printf("%d ", first[i]);
	}

		
    	pthread_t pid1, pid2, pid3;//creating a unique data type for threads

	pthread_create(&pid1, NULL, SortArrays, first);
	pthread_join(pid1, NULL);
	printf("\nSorted Half Array:\n");
	for(int x = 0; x < half_size; x++){
		printf("%d ", first[x]);
	}


	
	
	int count = 0;
	printf("\nOther half of array unsorted\n");
	for(int i = half_size; i < arr_size; i++){
		half[count] = arr[i];
		printf("%d ", half[count]);
		count++;
	}


	pthread_create(&pid2, NULL, SortArrays, half);
	pthread_join(pid2, NULL);
	printf("\nOther Sorted Half Array:\n");
	for(int x = 0; x < half_size; x++){
		printf("%d ", half[x]);
	}

	for(int x = 0; x < arr_size; x++){
		sort[x] = first[x];
	}

	int q = 0;
	for(int x = half_size; x < arr_size; x++){
		sort[x] = half[q];
		q++;
	}
	
	
	pthread_create(&pid3, NULL, fullSort, sort);
	pthread_join(pid3, NULL);
	printf("\nSorted new array...\n");
	for(int i = 0; i < arr_size; i++){
		printf("%d, ", sort[i]);
	}
	
	
	return 0;
}
