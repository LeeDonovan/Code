#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

struct Block {
    int block_size;
    struct Block *next_block;
};

void* my_alloc(int size);
int overhead_size = sizeof(struct Block);

int pointer_size = sizeof(void*);

struct Block *free_head;

void my_initialize_heap(int size){
    
    free_head = (struct Block *)malloc(size);
    free_head->block_size = size;
    free_head->next_block = NULL;
}

void* my_alloc(int size){
    int data_size = 0;
    if((size % pointer_size) >= 0){// checks if data size is a multiple of pointer size
        data_size = ceil((float)size / (float)pointer_size); //divides and rounds up size
        data_size = (int)data_size * pointer_size;//makes data size have extra room
    }
    if(data_size == 0){//if size is some how smaller than 0
        data_size = size * pointer_size;
        //this cheeses so that data_size will always be a multiple :)
    }
    struct Block *first = free_head; //this will be changed later on
    struct Block *prev = NULL; // space holder
    while(first){
        if(first->block_size >= data_size){
            if(first->block_size >= data_size + overhead_size){
                //we split 
                struct Block *temp = ((struct Block*)(char*)first + data_size + overhead_size);
                int temp_size = temp->block_size - data_size - overhead_size;//shrink temp's size
                if(temp_size >= data_size + overhead_size){//checks to make sure split was successful
                    temp_size = temp_size - data_size - overhead_size;
                }
                temp->block_size = temp_size;//shrunken block size
                temp->next_block = first->next_block;//first block splits into two parts 
                                                    //where first has one half and next block has the other
                first->block_size = data_size;//kept as the OG size
                first->next_block = temp;//first->next_block is null so temp->next_block holds a null
                //makes sure that first block was updated
                if(first != free_head){
                    //traverses and links next blocks
                    temp->next_block = first->next_block;
                    prev->next_block = temp;
                }
                else{//change free head to updated block
                    free_head = temp;
                }
            }
        }
        else{//first->block_size smaller than data_size
            if(first == free_head){// traversing through the list
                free_head = first->next_block;//go next block
            }
            else{//traverse through the list 
                prev->next_block = first->next_block;
            }
            first->next_block = NULL;//resets to NULL to be used again if needed
        }

        first = (struct Block*)((char*)first + overhead_size);//re-structure the block
        return first;//if i comment this return my system crashes for some reason?
        

    }
    //return first;//if this is the only return i crash for some reason?
}

void my_free(void *data){
    struct Block *free = data - overhead_size;//deallocates the data on the heap
    if (free_head != NULL){
        if(free > free_head){
            struct Block *temp = free_head;//sets the head block
            while(temp->next_block < free){
                temp = temp->next_block;
            }
            if(temp->next_block < free){//checks to make sure temp next is actually lower
                free->next_block = temp->next_block;
                temp->next_block = temp;
            }
        }
        else{
            if(free_head != free){
                free_head = free;
            }
            if(free->next_block != NULL){
                free->next_block = NULL;
            }
            
        }
    }
    else{
        if(free_head != free){//checks to make sure free_head was updated
            free_head = free;
        }
        if(free->next_block != NULL){
                free->next_block = NULL;
        }
    }
}

void testOne(){
    printf("\tTest One\n");
    printf("-------------------------\n");
    int *x = my_alloc(sizeof(int));
    printf("Address of x: %p\n",x);
    my_free(x);
    int *y = my_alloc(sizeof(int));
    printf("Address of y: %p",y);
    my_free(y);
}

void testTwo(){
    printf("\tTest Two\n");
    printf("-------------------\n");
    int *x = my_alloc(sizeof(int));
    int *y = my_alloc(sizeof(int));
    printf("Address of x: %p\n",x);
    printf("Address of y: %p\n",y);
    printf("Overhead + larger of (the size of an int) =  %d", overhead_size + sizeof(void*));
}

void testThree(){
    printf("\tTest Three\n");
    printf("-------------------------\n");
    int *x = my_alloc(sizeof(int));
    int *y = my_alloc(sizeof(int));
    int *z = my_alloc(sizeof(int));
    printf("Address of x: %p\n",x);
    printf("Address of y: %p\n",y);
    printf("Address of z: %p\n",z);

    my_free(y);
    printf("B has been freed!!!\n");
    double *array = my_alloc(2 * sizeof(double));
    printf("Address of double array: %p\n",z);
    int *a = my_alloc(sizeof(int));
    printf("Address: %p\n",a);

}

void testFour(){
    printf("\tTest Four\n");
    printf("-------------------------\n");
    char *x = my_alloc(sizeof(char));
    int *y = my_alloc(sizeof(int));
    printf("Address of char: %p\n",x);
    printf("Address of int: %p\n",y);
}

void testFive(){
    printf("\tTest Five\n");
    printf("-------------------------\n");
    int *x = my_alloc(80 * sizeof(int));
    printf("Address of int array: %p\n",x);

    int *y = my_alloc(sizeof(int));
    printf("Address of int: %p\n",y);

    printf("Address of int value 80 * sizeof(int) + size of header: %p\n",(x + (80 * sizeof(int))));
    printf("Address of y: %p\n",y);
    my_free(x);
    printf("After Freeing int\n");
    printf("Address of int: %p\n", x);
    printf("Address of int array: %p\n", y);


}

int menu(){
    int ans;
    printf("\nMain Menu\n");
    printf("1. Test One\n");
    printf("2. Test Two\n");
    printf("3. Test Three\n");
    printf("4. Test Four\n");
    printf("5. Test Five\n");
    printf("6. Quit\n");
    printf("Enter a number 1-6:\n");
    do{
        scanf("%d",&ans);
    }while(ans < 1 || ans > 6);
    return ans;

}  

int main(){
    int ans;
    bool check = true;
    while(check){
        my_initialize_heap(1000);
        ans = menu();
        if(ans == 1){
            testOne();
        }
        if(ans == 2){
            testTwo();
        }
        if(ans == 3){
            testThree();
        }
        if(ans == 4){
            testFour();
        }
        if(ans == 5){
            testFive();
        }
        if(ans == 6){
            printf("Goodybye...");//must restart each time to reset heap
            check = false;
        }
    }


    


    return 0;
}