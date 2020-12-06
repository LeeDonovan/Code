/**
 * RR scheduling
 */
 
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "task.h"
#include "list.h"
#include "cpu.h"
int TID = 1;
//Your code and design here
struct node *head = NULL;
void add(char *name, int priority, int burst);

void add(char *name, int priority, int burst){
    Task *addTask = malloc(sizeof(Task));//allocate space for Task
    addTask->name = name;//add name
    addTask->tid = TID;//add ID
    addTask->priority = priority;//add priority
    addTask->burst = burst;//add burst
    TID++;

    if(head == NULL){
        head = (struct node*)malloc(sizeof(struct node));//allocate space for top of empty node
        head->task = addTask;
        head->next = NULL;
        
    }
    else{
        insert(&head, addTask);//insert new task created 
        
    }
}


void schedule(){
	struct node *first = head;//set a duplicate of head node
	bool x = true;
	int max = 1;
	while(x){
		if(head == NULL){//checks to see if head is null if loop is finished going next
			head = first;//resets head to beginning
		}
		
		if(head->task->burst >= 10){//if burst is greater than or equal to 10
			run(head->task, 10);
			head->task->burst = head->task->burst - 10;//subtracts by 10 
			if(head->task->burst == 0){
				printf("Task %s finished\n", head->task->name);
				max++;
				if(max == TID){
					x = false;//loop breaks if all task are finished
				}
			}
			else{
				head = head->next;
			}
			
			
		}
		else if ((head->task->burst >0 ) && (head->task->burst <=9)){//if burst is below 10
			run(head->task,head->task->burst);
			head->task->burst = head->task->burst - head->task->burst;//subtract by same burst to get 0
			printf("Task %s finished\n", head->task->name);
			max++;
			if(max ==TID){//checks to see if we finished all node burst
				x = false;
			}
			else{
				head = head->next;
			}
			
		

		}
		else if(head->task->burst == 0){//if burst is 0 then we skip that node
			head = head->next;
			if(max == TID){
				x = false;
			}
		}
		else{
		printf("All Task Completed...\n");
		x = false;
		}
	}
	
}